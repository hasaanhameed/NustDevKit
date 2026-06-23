// Injects APIMatic's real, rendered SDK code samples into the Scalar docs artifact.
//
// Source of truth for the samples: the committed SDK zips under portal/static/sdks/.
// Each zip ships doc/controllers/<tag>.md with a uniform per-endpoint layout:
//
//   # <Endpoint Title>
//   ...
//   Moodle method: `core_course_get_recent_courses`   <- maps to the spec path
//   ```<lang>                                          <- method signature (skipped)
//   ...
//   ```
//   ## Example Usage
//   ```<lang>                                          <- the real example (extracted)
//   ...
//   ```
//
// We extract the Example Usage block per endpoint per language and attach it as
// x-codeSamples on the matching operation in docs/openapi.yaml. The canonical
// src/spec/openapi.yaml stays clean; only the build artifact is enriched.
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import AdmZip from "adm-zip";
import { parse, stringify } from "yaml";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const specPath = resolve(root, "docs/openapi.yaml");
const sdksDir = resolve(root, "portal/static/sdks");

// zip basename -> { lang (for highlighting), label (tab text) }.
// Order of this map is the tab order shown in Scalar.
const LANGS = [
  ["ts_generic_lib", { lang: "typescript", label: "TypeScript" }],
  ["python_generic_lib", { lang: "python", label: "Python" }],
  ["java_eclipse_jre_lib", { lang: "java", label: "Java" }],
  ["cs_net_standard_lib", { lang: "csharp", label: ".NET (C#)" }],
  ["go_generic_lib", { lang: "go", label: "Go" }],
  ["php_generic_lib_v2", { lang: "php", label: "PHP" }],
  ["ruby_generic_lib", { lang: "ruby", label: "Ruby" }],
];

// Pull the first fenced code block that appears after the "## Example Usage"
// heading within a single endpoint section. Returns the code, fences stripped.
function extractExample(section) {
  const idx = section.indexOf("## Example Usage");
  if (idx === -1) return null;
  const after = section.slice(idx);
  const fence = after.match(/```[^\n]*\n([\s\S]*?)```/);
  return fence ? fence[1].replace(/\s+$/, "") : null;
}

// Pull the per-language "Client Initialization" snippet from an SDK's bearer-auth
// doc, swapping the placeholder token for a clearer name.
function extractClientInit(md) {
  const idx = md.indexOf("### Client Initialization");
  if (idx === -1) return null;
  const fence = md.slice(idx).match(/```[^\n]*\n([\s\S]*?)```/);
  if (!fence) return null;
  return fence[1].replace(/\s+$/, "").split("AccessToken").join("YOUR_BEARER_TOKEN");
}

// Single-line comment marker for a language (used when stitching snippets).
const lineComment = (lang) => (lang === "python" || lang === "ruby" ? "#" : "//");

// Parse one controller markdown into { moodleMethod -> exampleCode }.
function parseController(md) {
  const out = {};
  // Split on h1 headings; each endpoint lives in its own "# <Title>" section.
  const sections = md.split(/\n(?=# )/);
  for (const section of sections) {
    const m = section.match(/Moodle method:\s*`([^`]+)`/);
    if (!m) continue;
    const code = extractExample(section);
    if (code) out[m[1]] = code;
  }
  return out;
}

// Read all controller docs from one SDK zip -> { moodleMethod -> exampleCode }.
function samplesFromZip(zipName) {
  const zip = new AdmZip(resolve(sdksDir, `nust-lms-api-${zipName}.zip`));
  const out = {};
  for (const entry of zip.getEntries()) {
    if (/^doc\/controllers\/.+\.md$/.test(entry.entryName)) {
      Object.assign(out, parseController(entry.getData().toString("utf8")));
    }
  }
  return out;
}

// --- Build the per-method sample tables, one per language. ---
const byLang = LANGS.map(([zipName, meta]) => ({
  meta,
  samples: samplesFromZip(zipName),
}));

// --- Inject into the spec artifact. ---
const spec = parse(readFileSync(specPath, "utf8"));
const errors = [];

for (const [path, ops] of Object.entries(spec.paths ?? {})) {
  // Only the proxied LMS endpoints map to an APIMatic SDK method. Skip gateway
  // operations like /auth/login, which have no generated SDK code sample.
  if (!path.startsWith("/service/")) continue;
  // Spec paths are /service/<moodle_method>. Reads are GET; fall back to POST.
  const moodleMethod = path.replace(/^\/service\//, "");
  const op = ops.get ?? ops.post;
  if (!op) continue;

  const codeSamples = [];
  for (const { meta, samples } of byLang) {
    const source = samples[moodleMethod];
    if (!source) {
      errors.push(`missing ${meta.label} sample for ${path}`);
      continue;
    }
    if (source.includes("{%")) {
      errors.push(`unrendered Liquid leaked into ${meta.label} sample for ${path}`);
      continue;
    }
    codeSamples.push({ lang: meta.lang, label: meta.label, source });
  }
  op["x-codeSamples"] = codeSamples;
}

// Login isn't a Moodle method (no /service/ path), so inject its sample
// separately from the SDK's Authentication controller doc. Best-effort: if the
// SDKs don't ship that controller yet (e.g. before a regeneration), login simply
// renders without code samples rather than failing the build.
const loginOp = spec.paths?.["/auth/login"]?.post;
const initSamples = [];
if (loginOp) {
  const loginSamples = [];
  for (const [zipName, meta] of LANGS) {
    const zip = new AdmZip(resolve(sdksDir, `nust-lms-api-${zipName}.zip`));
    const callEntry = zip.getEntry("doc/controllers/authentication.md");
    const authEntry = zip.getEntry("doc/auth/oauth-2-bearer-token.md");
    const call = callEntry ? extractExample(callEntry.getData().toString("utf8")) : null;
    const init = authEntry ? extractClientInit(authEntry.getData().toString("utf8")) : null;
    if (call && !call.includes("{%")) {
      loginSamples.push({ lang: meta.lang, label: meta.label, source: call });
    }
    if (init && !init.includes("{%")) {
      initSamples.push({ lang: meta.lang, label: meta.label, source: init });
    }
  }
  if (loginSamples.length) loginOp["x-codeSamples"] = loginSamples;
}

// Docs-only "SDK Setup" section: a sidebar entry in the Getting Started group whose
// code panel is the tabbed per-language client-init. Injected into the docs artifact
// only (never src), so APIMatic never generates a method for it.
if (initSamples.length) {
  spec.paths["/sdk/initialize-client"] = {
    get: {
      operationId: "initializeSdkClient",
      summary: "Initialize the SDK client",
      tags: ["SDK Setup"],
      security: [],
      description:
        "Setup reference (not a live endpoint). After installing an SDK and getting a " +
        "token from `POST /auth/login`, initialize a client with that token — every " +
        "other code sample assumes this `client`.",
      "x-codeSamples": initSamples,
      responses: {
        "200": {
          description:
            "This section documents client initialization; it is not a callable endpoint.",
        },
      },
    },
  };

  spec.tags = spec.tags ?? [];
  if (!spec.tags.some((t) => t.name === "SDK Setup")) {
    spec.tags.push({
      name: "SDK Setup",
      description: "Install an SDK and initialize a client with your bearer token.",
    });
  }
  const gs = (spec["x-tagGroups"] ?? []).find((g) => g.name === "Getting Started");
  if (gs && !gs.tags.includes("SDK Setup")) gs.tags.push("SDK Setup");
}

// Append a "Getting Started" section to info.description: per-language SDK download
// link + concise install command (the SDKs are unpublished, so install is from the
// downloaded folder). The per-language init CODE lives (tabbed) in the SDK Setup section.
// Concise, IDE-neutral install steps so users don't need each SDK's (PyCharm-flavoured)
// README. Keyed by zip basename.
const INSTALL = {
  python_generic_lib: "run `pip install -r requirements.txt` in the unzipped folder",
  ts_generic_lib: "run `npm install` in the unzipped folder, then add it to your project",
  php_generic_lib_v2: "run `composer install` in the unzipped folder",
  ruby_generic_lib: "run `gem build nust_lms_api.gemspec && gem install nust_lms_api-1.0.0.gem`",
  go_generic_lib: "add a local `replace` for the folder in your `go.mod`, then run `go get`",
  cs_net_standard_lib: "add a project reference to the `NustLmsApi.Standard` project",
  java_eclipse_jre_lib: "build the JAR with Gradle and add it to your project",
};

const sdkItems = LANGS.filter(([zipName]) =>
  existsSync(resolve(sdksDir, `nust-lms-api-${zipName}.zip`))
).map(
  ([zipName, meta]) =>
    `   - **${meta.label}** — [download](./sdks/nust-lms-api-${zipName}.zip), then ` +
    `${INSTALL[zipName] ?? "install from the unzipped folder (see its README)"}.`
);

if (sdkItems.length && spec.info) {
  const gettingStarted = [
    "",
    "## Getting Started with the SDKs",
    "",
    "1. **Get the SDK** for your language — download the zip, unzip it, and install it:",
    ...sdkItems,
    "2. **Get a bearer token** from `POST /auth/login` with your NUST LMS credentials.",
    "3. **Initialize a client** with that token — see the **SDK Setup** section for the",
    "   per-language code. Every other sample assumes that `client`.",
    "",
    "_Each SDK's own README has fuller, IDE-specific setup if you want it._",
    "",
  ].join("\n");
  spec.info.description = `${(spec.info.description ?? "").trimEnd()}\n${gettingStarted}\n`;
}

if (errors.length) {
  console.error("✗ Code-sample injection failed:");
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}

const total = Object.values(spec.paths).filter(
  (o) => (o.get ?? o.post)?.["x-codeSamples"]
).length;
writeFileSync(specPath, stringify(spec, { lineWidth: 0 }), "utf8");
console.log(
  `✓ Injected x-codeSamples (${byLang.length} langs) into ${total} operation(s) → docs/openapi.yaml`
);
