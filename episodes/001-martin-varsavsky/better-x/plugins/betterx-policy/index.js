import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";

const WRITE_VERBS = new Set([
  "post",
  "quote",
  "reply",
  "follow",
  "like",
  "repost",
  "block",
  "dm",
  "delete",
  "unfollow",
  "unlike",
  "unrepost",
]);

const OPTION_WITH_VALUE = new Set([
  "--app",
  "--user",
  "--bearer-token",
  "--access-token",
  "--access-secret",
  "--consumer-key",
  "--consumer-secret",
  "--client-id",
  "--client-secret",
  "--redirect-uri",
  "-n",
  "--max-results",
]);

function flatten(value) {
  if (typeof value === "string") {
    return value;
  }
  if (Array.isArray(value)) {
    return value.map(flatten).join(" ");
  }
  if (value && typeof value === "object") {
    return Object.values(value).map(flatten).join(" ");
  }
  return "";
}

function argvFromToolParams(params) {
  const raw = params.cmd ?? params.command ?? params.argv ?? params.args ?? params.input;
  if (Array.isArray(raw)) {
    return raw.map((part) => String(part));
  }
  return flatten(raw).split(/\s+/).filter(Boolean);
}

function verbFromArgv(argv) {
  let i = 0;
  while (i < argv.length) {
    const part = argv[i] ?? "";
    if (OPTION_WITH_VALUE.has(part)) {
      i += 2;
      continue;
    }
    if (part.startsWith("-")) {
      i += 1;
      continue;
    }
    return part;
  }
  return "";
}

function commandMentionsXurl(text) {
  return /(^|\s)(xurl|\/opt\/homebrew\/bin\/xurl|\/usr\/local\/bin\/xurl)(\s|$)/.test(text);
}

function commandUsesBetterXApp(text, appAliases) {
  if (appAliases.length === 0) {
    return true;
  }
  return appAliases.some((alias) => text.includes(alias));
}

function commandUsesActionGate(text, actionGatePaths) {
  if (text.includes("betterx_action_gate.py")) {
    return true;
  }
  return actionGatePaths.some((path) => path && text.includes(path));
}

export default definePluginEntry({
  id: "betterx-policy",
  name: "BetterX Policy Gate",
  description: "Blocks raw X write commands unless BetterX action-gate execution is detected.",
  register(api) {
    api.on(
      "before_tool_call",
      async (event) => {
        const cfg = event.context?.pluginConfig ?? {};
        if (cfg.enabled === false) {
          return;
        }
        if (event.toolName !== "exec" && event.toolKind !== "code_mode_exec") {
          return;
        }

        const params = event.params ?? {};
        const argv = argvFromToolParams(params);
        const commandText = flatten(params);
        if (!commandMentionsXurl(commandText)) {
          return;
        }
        if (!commandUsesBetterXApp(commandText, cfg.appAliases ?? [])) {
          return;
        }
        if (commandUsesActionGate(commandText, cfg.actionGatePaths ?? [])) {
          return;
        }

        const verb = verbFromArgv(argv);
        const hasWriteVerb =
          WRITE_VERBS.has(verb) ||
          Array.from(WRITE_VERBS).some((writeVerb) => new RegExp(`(^|\\s)${writeVerb}(\\s|$)`).test(commandText));

        if (!hasWriteVerb) {
          return;
        }

        return {
          block: true,
          blockReason:
            "BetterX blocks raw xurl write commands. Use scripts/betterx_action_gate.py with a validated review artifact.",
        };
      },
      { priority: 1000, timeoutMs: 1000 },
    );
  },
});
