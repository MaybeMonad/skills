import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";
import path from "node:path";
import fs from "node:fs";

const skillRequire = createRequire(import.meta.url);

function requireFromCwd() {
  const packagePath = path.join(process.cwd(), "package.json");
  if (!fs.existsSync(packagePath)) return null;
  return createRequire(pathToFileURL(packagePath));
}

export function loadPlaywright() {
  const envPath = process.env.PLAYWRIGHT_MODULE_PATH;
  const cwdRequire = requireFromCwd();
  const attempts = [
    () => (envPath ? skillRequire(envPath) : null),
    () => (cwdRequire ? cwdRequire("playwright") : null),
    () => skillRequire("playwright"),
  ];

  for (const attempt of attempts) {
    try {
      const result = attempt();
      if (result) return result;
    } catch {
      // Try the next resolution path.
    }
  }

  throw new Error(
    "Playwright not found. Run `npm install -D playwright` in the clone project, or set PLAYWRIGHT_MODULE_PATH to an installed playwright module."
  );
}

export async function launchChromium(chromium) {
  try {
    return await chromium.launch({ headless: true });
  } catch (firstError) {
    try {
      return await chromium.launch({ headless: true, channel: "chrome" });
    } catch {
      throw firstError;
    }
  }
}
