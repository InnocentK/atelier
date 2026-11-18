---
type: doc
created: 2026-09-16
vault: agent-org
---

# Agent Org

Agent Org is an **agent-curated organizational vault**. Humans are primarily readers and decision owners. Agents perform most intake and maintenance, but they do so through a strict Curator → transaction → Vault Operator path.

This vault is **not** a personal operations vault. A personal vault (see the `personal-ops` environment) holds reminders, contacts, and calendar-style planning. This vault holds organizational artifacts: org structure, project outcomes, operations evidence, research, decisions, and reports. Privacy boundary, authority model, and retention differ.

Local path (canonical): `/absolute/path/to/this/vault`

Cloud: **Obsidian Sync**, enrolled by a human through the official application. Credentials never belong here.

Three root files define the vault: [[README]] (this file) describes structure, [[AGENTS]] is the operating manual every agent must follow, and [[CLAUDE]] points at [[AGENTS]] with Claude-specific mechanics.

## Canonical truth

Repositories, task board databases, exact revisions, profile workspaces, and verified source artifacts remain authoritative. A note here is a curated human-readable copy or synthesis. It must never silently replace or contradict its source.

## Layout

| Folder | Contains |
| --- | --- |
| `Inbox/Manifests/` | Submission manifests from task board. Not long-term storage. |
| `Quarantine/` | Rejected, drifted, secret-scan-failed, or rolled-back material. Not published. |
| `Transactions/Pending/` | Curator-approved transaction files awaiting Operator execution. |
| `Transactions/Receipts/` | Non-secret execution receipts and preimages. |
| `Organization/Org Chart/` | Curated org-chart notes. Source HTML/repo remains authoritative. |
| `Organization/Role Registry/` | Role/profile registry copies. |
| `Organization/Host Registry/` | Host placement notes. |
| `Projects/Example/` | One project's artifacts. |
| `Operations/IT/` | IT evidence and change receipts (non-secret). |
| `Operations/Security/` | Security verdicts and audits (non-secret). |
| `Operations/Secrets-Metadata/` | Non-secret metadata only: that a secret exists elsewhere, owner, rotation cadence. Never values. |
| `Research/` | Researcher and Informer curated reports. |
| `Decisions/` | Recorded organizational decisions. |
| `Reports/` | Cross-cutting reports. |
| `Catalog/` | Indexes by profile, project, and evidence type. |
| `Templates/` | Note skeletons. |
| `Meta/` | Schema, registry, retention, Sync, sensitivity, conflict, and intake-gate policy. |
| `Archive/` | Non-destructive historical copies, still readable. |
| `Trash/` | Staged purge recommendations. Only the human empties it. |

`.obsidian/` is app configuration, not content. Agents never touch it, `.trash/`, or other dotfiles.

Obsidian Sync does not propagate empty folders. Each folder therefore contains `_Keep.md` until real notes exist.

## Naming

Dates are **YYYY-MM-DD** in filenames and date properties. Times are 24-hour `"HH:MM"` in Your/Timezone unless a note says otherwise.

Filenames use letters, digits, spaces, and hyphens. Avoid `# ^ [ ] | / \\ :`. Basenames must be unique across the vault so wikilinks resolve, except official Sync conflict copies whose names include `(Conflicted copy ...)`.

Do not repeat the filename as an `# H1`. Bodies start with content or `##` sections.

## Properties

Every note has YAML frontmatter with `type`. Allowed types are listed in [[Artifact Schema]]. Properties make the vault filterable with core Bases. Do not invent types or properties without a Curator policy change approved by the human.

## Linking

Use `[[wikilinks]]`. Inside properties, quote them: `related: ["[[Artifact Schema]]"]`.

Moving a note keeps wikilinks. Renaming outside Obsidian breaks inbound links — search and update, or do not rename.

## Tags

Folders, `type`, `state`, and `sensitivity` already encode most slicing. Optional lowercase-kebab tags may mark cross-cutting themes. Never duplicate folder or type as a tag.

## Archive, Trash, deletion

- Archive is a non-destructive move to `Archive/` on Curator approval.
- `Trash/` is a purge recommendation, not deletion. It requires Curator plus source owner/manager concurrence (Orchestrator only if that owner is unavailable). Security-sensitive cases may need Security Auditor review.
- Permanent purge and emptying `Trash/` are human-only. Agents never delete user data.

## Isolation (honest bound)

Agent runtimes and the human's Obsidian app may run as the same operating-system user. This vault's control is policy plus a deterministic broker and audit trail. Unauthorized same-UID writes are detectable; they are not OS-prevented. Do not claim hard isolation.

## Obsidian setup (human / official UI only)

Keep the vault close to default core behavior:

- Core plugins only. Sync is required. Community plugins are out of scope.
- Settings → Templates → Template folder location: `Templates`.
- Settings → Sync → Conflict resolution: **Create conflict file** on every device.
- Agents never edit `.obsidian/`.
