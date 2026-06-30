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
// x-codeSamples on the matching operation in ndk_frontend/openapi.yaml. The canonical
// src/spec/openapi.yaml stays clean; only the build artifact is enriched.
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import AdmZip from "adm-zip";
import { parse, stringify } from "yaml";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const specPath = resolve(root, "ndk_frontend/openapi.yaml");
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

// The very first fenced block in a controller doc. APIMatic puts the controller
// handle there (e.g. `authentication_api = client.authentication`) right under the
// "# <Controller>" heading — extractExample drops it, so capture it separately.
function controllerVarLine(md) {
  const fence = md.match(/```[^\n]*\n([\s\S]*?)```/);
  return fence ? fence[1].trim() : null;
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

// Per-language test for "this line is an import" (line-based langs; Go is handled
// separately because its imports live in a parenthesised block).
const IMPORT_RE = {
  typescript: /^import\b/,
  python: /^(import|from)\b/,
  java: /^import\b/,
  csharp: /^using\b/,
  php: /^use\b/,
  ruby: /^require\b/,
};

// Single-line comment marker for a language.
const lineComment = (lang) => (lang === "python" || lang === "ruby" ? "#" : "//");

// Split a code block into { imports, body } for line-based languages.
function splitImports(code, lang) {
  const re = IMPORT_RE[lang];
  if (!re) return { imports: [], body: code.trim() };
  const imports = [];
  const body = [];
  for (const raw of code.split("\n")) {
    if (re.test(raw.trim())) imports.push(raw.trim());
    else body.push(raw);
  }
  return { imports, body: body.join("\n").replace(/^\n+|\n+$/g, "") };
}

// Parse a controller doc into its handle line + { moodleMethod -> exampleCode }.
function parseController(md) {
  const controllerLine = controllerVarLine(md);
  const methods = {};
  for (const section of md.split(/\n(?=# )/)) {
    const m = section.match(/Moodle method:\s*`([^`]+)`/);
    if (!m) continue;
    const code = extractExample(section);
    if (code) methods[m[1]] = code;
  }
  return { controllerLine, methods };
}

// Build a line-based language's model-import index: { ModelName -> [import lines] }.
// Extracted from each model doc's "## Example" block (which ships the real import),
// keeping only the line(s) naming the model so unrelated helpers (jsonpickle,
// ApiHelper, ...) don't leak in.
function modelsFromZip(zip, lang) {
  const out = {};
  for (const entry of zip.getEntries()) {
    if (!/^doc\/models\/.+\.md$/.test(entry.entryName)) continue;
    const md = entry.getData().toString("utf8");
    // Model name from the kebab-case filename (enums lack a "## Structure" heading,
    // so deriving from the filename indexes models and enums uniformly).
    const name = entry.entryName
      .replace(/^.*\//, "")
      .replace(/\.md$/, "")
      .split("-")
      .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
      .join("");
    const exIdx = md.indexOf("## Example");
    if (exIdx === -1) continue;
    const fence = md.slice(exIdx).match(/```[^\n]*\n([\s\S]*?)```/);
    if (!fence) continue;
    const { imports } = splitImports(fence[1], lang);
    // C# documents the model via its namespace (`using ...Models;`) with no class
    // name, so match the Models namespace there; class-import langs (py/ts/java/php)
    // carry the class name in the line itself.
    const own =
      lang === "csharp"
        ? imports.filter((l) => /\.Models\b/.test(l))
        : imports.filter((l) => l.includes(name));
    if (own.length) out[name] = own;
  }
  return out;
}

// Go import paths referenced by a snippet. `base` is the SDK module path (e.g.
// "nustLmsApi"), taken from an extracted Go import.
function goImports(snippet, base) {
  const map = {
    "context.": "context",
    "fmt.": "fmt",
    "log.": "log",
    "models.": `${base}/models`,
    "errors.": `${base}/errors`,
  };
  const used = [];
  for (const [tok, path] of Object.entries(map)) {
    if (snippet.includes(tok) && !used.includes(path)) used.push(path);
  }
  const std = used.filter((p) => !p.includes("/")); // stdlib grouped first (gofmt)
  const mod = used.filter((p) => p.includes("/"));
  return [...std, ...mod];
}

// Assemble a usable sample: the imports the call needs + the controller handle +
// the call. The `client` itself comes from the SDK Setup section (one place), so a
// leading comment points there rather than repeating client init in every sample.
function assemble({ lang, controllerLine, call, modelIndex, base, comment }) {
  const head = comment ? `${comment}\n` : "";
  // Some langs (e.g. PHP) already include the controller handle in their Example
  // Usage — don't prepend a duplicate.
  const handle = controllerLine && !call.includes(controllerLine) ? `${controllerLine}\n\n` : "";
  if (lang === "go") {
    const paths = goImports(`${controllerLine}\n${call}`, base);
    const block = paths.length
      ? `import (\n${paths.map((p) => `    "${p}"`).join("\n")}\n)\n\n`
      : "";
    return `${block}${head}${handle}${call}`;
  }
  // Match against code with string literals blanked out, so a type name that only
  // appears inside a string (e.g. PHP `echo 'TokenResponse:'`) doesn't pull an
  // unused import.
  const code = call.replace(/'[^']*'/g, "''").replace(/"[^"]*"/g, '""');
  const used = new Set();
  for (const name of Object.keys(modelIndex)) {
    // Word-boundary match so e.g. `Course` doesn't match inside
    // `CourseTimelineClassification`; allow a trailing `Builder` (PHP uses
    // `LoginRequestBuilder` for model `LoginRequest`).
    if (new RegExp(`\\b${name}(?:Builder)?\\b`).test(code)) {
      for (const imp of modelIndex[name]) used.add(imp);
    }
  }
  const imports = used.size ? `${[...used].join("\n")}\n\n` : "";
  return `${imports}${head}${handle}${call}`;
}

// --- Build the per-language extraction tables from each SDK zip. ---
const byLang = LANGS.map(([zipName, meta]) => {
  const zip = new AdmZip(resolve(sdksDir, `nust-lms-api-${zipName}.zip`));
  const lang = meta.lang;

  // Controller docs -> per-method { example, controllerLine }, plus the login bits.
  const byMethod = {};
  let authControllerLine = null;
  let loginExample = null;
  for (const entry of zip.getEntries()) {
    if (!/^doc\/controllers\/.+\.md$/.test(entry.entryName)) continue;
    const md = entry.getData().toString("utf8");
    const { controllerLine, methods } = parseController(md);
    for (const [m, ex] of Object.entries(methods)) byMethod[m] = { example: ex, controllerLine };
    if (/\/authentication\.md$/.test(entry.entryName)) {
      authControllerLine = controllerLine;
      // Login has no "Moodle method:" line, so grab its "# Login" section directly.
      const sec = md.split(/\n(?=# )/).find((s) => /^# Login\b/m.test(s));
      loginExample = sec ? extractExample(sec) : null;
    }
  }

  // Full client-init snippet (with imports) for the SDK Setup section.
  const authEntry = zip.getEntry("doc/auth/oauth-2-bearer-token.md");
  const initRaw = authEntry ? extractClientInit(authEntry.getData().toString("utf8")) : null;

  // Model imports (line langs) and the Go module base for building Go import blocks.
  const modelIndex = lang === "go" ? {} : modelsFromZip(zip, lang);
  let base = "";
  if (lang === "go" && initRaw) {
    const mm = initRaw.match(/"([^"]+)"/); // first quoted import in the Go client init
    base = mm ? mm[1] : "";
  }

  return { meta, lang, byMethod, authControllerLine, loginExample, initRaw, modelIndex, base };
});

// --- Inject into the spec artifact. ---
const spec = parse(readFileSync(specPath, "utf8"));
const errors = [];
// Missing SDK samples are non-fatal: a newly-added endpoint has no generated
// sample until the SDKs are regenerated via APIMatic. The operation still renders
// (without a Code Examples panel) and gains samples on the next regeneration.
const warnings = [];

for (const [path, ops] of Object.entries(spec.paths ?? {})) {
  // Only the proxied LMS endpoints map to an APIMatic SDK method. Skip gateway
  // operations like /auth/login, which have no generated SDK code sample.
  if (!path.startsWith("/service/")) continue;
  // Spec paths are /service/<moodle_method>. Reads are GET; fall back to POST.
  const moodleMethod = path.replace(/^\/service\//, "");
  const op = ops.get ?? ops.post;
  if (!op) continue;

  const codeSamples = [];
  for (const L of byLang) {
    const entry = L.byMethod[moodleMethod];
    if (!entry) {
      warnings.push(`missing ${L.meta.label} sample for ${path} (regenerate SDKs)`);
      continue;
    }
    if (entry.example.includes("{%")) {
      errors.push(`unrendered Liquid leaked into ${L.meta.label} sample for ${path}`);
      continue;
    }
    const source = assemble({
      lang: L.lang,
      controllerLine: entry.controllerLine,
      call: entry.example,
      modelIndex: L.modelIndex,
      base: L.base,
      comment: `${lineComment(L.lang)} Uses the configured \`client\` from the SDK Setup section.`,
    });
    codeSamples.push({ lang: L.lang, label: L.meta.label, source });
  }
  // Only attach when we actually have samples — a new endpoint awaiting SDK
  // regeneration shouldn't render an empty Code Examples panel.
  if (codeSamples.length) op["x-codeSamples"] = codeSamples;
}

// Login isn't a Moodle method (no /service/ path), so inject its sample
// separately from the SDK's Authentication controller doc. Best-effort: if the
// SDKs don't ship that controller yet (e.g. before a regeneration), login simply
// renders without code samples rather than failing the build.
const loginOp = spec.paths?.["/auth/login"]?.post;
const initSamples = [];
if (loginOp) {
  const loginSamples = [];
  for (const L of byLang) {
    if (L.initRaw && !L.initRaw.includes("{%")) {
      initSamples.push({ lang: L.lang, label: L.meta.label, source: L.initRaw });
    }
    if (!L.loginExample || !L.authControllerLine || L.loginExample.includes("{%")) continue;
    const source = assemble({
      lang: L.lang,
      controllerLine: L.authControllerLine,
      call: L.loginExample,
      modelIndex: L.modelIndex,
      base: L.base,
      comment:
        `${lineComment(L.lang)} No token needed to log in — create a \`client\` per the ` +
        `SDK Setup section, then call this to get your token.`,
    });
    loginSamples.push({ lang: L.lang, label: L.meta.label, source });
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
      // No `responses` — this is a docs-only setup section, not a callable endpoint,
      // so Scalar renders no "Responses / 200" block for it.
      responses: {},
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
    "2. **Get a bearer token** — call `POST /auth/login` with your NUST LMS credentials",
    "   (no token needed for this call). See the **login** operation's Code Examples for a",
    "   per-language snippet, and read `access_token` off the response.",
    "3. **Initialize a client** with that token — see the **SDK Setup** section. Every other",
    "   sample's `client` comes from there.",
    "4. **Call an endpoint** — each operation's Code Examples include the imports it needs,",
    "   the controller handle, and the call.",
    "",
    "_Each SDK's own README has fuller, IDE-specific setup if you want it._",
    "",
  ].join("\n");
  spec.info.description = `${(spec.info.description ?? "").trimEnd()}\n${gettingStarted}\n`;
}

// Append the "Connect an AI assistant (MCP)" section AFTER the SDK getting-started,
// so the overview reads SDKs first, then MCP. Static text (not derived from the SDKs),
// but appended here to control its order relative to the SDK block.
if (spec.info) {
  const mcpSection = [
    "",
    "## Connect an AI assistant (MCP)",
    "",
    "Beyond the SDKs, this API is also an **MCP server**, so AI assistants (Claude Code,",
    "Claude Desktop, Cursor, VS Code, Claude.ai, ChatGPT) can call it as tools — for",
    'example, *"what deadlines do I have this week?"*.',
    "",
    "Auth is handled for you by **OAuth 2.0 with PKCE** — you do **not** paste a bearer",
    "token. On first connect the client opens a hosted login page; enter your NUST LMS",
    "credentials there and it obtains its tokens automatically (the assistant never sees",
    "your password). Login is never an MCP tool.",
    "",
    "- **Endpoint:** `https://api.nustdevkit.com/mcp/`",
    "- **Transport:** Streamable HTTP",
    "",
    "**Desktop / editor clients** (Claude Code, Claude Desktop, Cursor, VS Code) — add the",
    "server to the client's MCP config; no token needed:",
    "",
    "```json",
    '{ "mcpServers": { "nust-lms": {',
    '    "type": "http",',
    '    "url": "https://api.nustdevkit.com/mcp/" } } }',
    "```",
    "",
    "**Web assistants** (Claude.ai, ChatGPT) — open Settings → Connectors, add a custom",
    "connector with the same URL `https://api.nustdevkit.com/mcp/`, then complete the login",
    "when prompted.",
    "",
  ].join("\n");
  spec.info.description = `${(spec.info.description ?? "").trimEnd()}\n${mcpSection}\n`;
}

if (errors.length) {
  console.error("✗ Code-sample injection failed:");
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}

if (warnings.length) {
  console.warn("! Code samples skipped (endpoint(s) awaiting SDK regeneration):");
  for (const w of warnings) console.warn(`  - ${w}`);
}

const total = Object.values(spec.paths).filter(
  (o) => (o.get ?? o.post)?.["x-codeSamples"]
).length;
writeFileSync(specPath, stringify(spec, { lineWidth: 0 }), "utf8");
console.log(
  `✓ Injected x-codeSamples (${byLang.length} langs) into ${total} operation(s) → ndk_frontend/openapi.yaml`
);
