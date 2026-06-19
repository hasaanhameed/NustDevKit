// Copies the canonical OpenAPI spec and branding assets into docs/ so the
// Scalar frontend has everything it needs as a self-contained static bundle.
// Single source of truth: src/spec/openapi.yaml — docs/openapi.yaml is a build artifact.
import { copyFileSync, mkdirSync, existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const docs = resolve(root, "docs");
mkdirSync(docs, { recursive: true });

const assets = [
  ["src/spec/openapi.yaml", "docs/openapi.yaml"],
  ["portal/static/images/nust-logo.png", "docs/nust-logo.png"],
  ["src/static/images/favicon.ico", "docs/favicon.ico"],
];

let copied = 0;
for (const [from, to] of assets) {
  const src = resolve(root, from);
  if (!existsSync(src)) {
    console.warn(`! skipped (missing): ${from}`);
    continue;
  }
  copyFileSync(src, resolve(root, to));
  console.log(`✓ ${from} → ${to}`);
  copied++;
}
console.log(`\nSynced ${copied}/${assets.length} asset(s) into docs/.`);
