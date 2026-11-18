---
type: doc
created: 2026-01-01
---

Every agent that writes to this vault is registered here before its first write, by the owner's decision — agents do not register themselves. The name in the first column is what appears in daily-log lines, e.g. `- 10:51 (claude) Created …`.

Rows are never deleted. A retired agent keeps its row with an end date in Status, because its old log lines must stay attributable forever.

| Name | Runtime | Write access | Since | Status |
| --- | --- | --- | --- | --- |
| `claude` | Example: an interactive assistant session with file access to the vault | read-write | 2026-01-01 | active |
| `ops-agent` | Example: a scheduled agent on a server (the name identifies the deployment, never the model) | read-write | 2026-01-01 | active |

Replace the example rows with your own. `Meta/check-log-agents.py` verifies the daily logs against this table — it parses the Name column as the allowlist, so adding a row here is the whole registration step. It runs as item 8 of the health check in [[AGENTS]].

Read-only agents (a morning brief, for example) never log because they never write, so they need no row.

If you sync with Obsidian Sync, non-markdown files such as the `.py` checker only travel when "Sync all other types" is enabled under Selective sync.
