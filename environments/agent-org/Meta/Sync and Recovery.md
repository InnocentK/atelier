---
type: schema
created: 2026-09-16
---

# Sync and Recovery

Provider: **Obsidian Sync** only. No third-party folder sync (iCloud/Dropbox/Drive) on this vault path.

## Enrollment

Human-only through official Obsidian UI. See the governance package `handoff/obsidian-human-auth.md`. Agents never receive passwords, encryption passwords, recovery material, or 2FA codes.

Do not use Obsidian Headless for this vault.

## Device settings (human, official UI)

On every device that opens this vault:

1. Core plugin **Sync** enabled.
2. Conflict resolution: **Create conflict file** (Obsidian ≥ 1.9.7). Not "Automatically merge".
3. Device name set so conflict copies and Sync logs are attributable.
4. Selective sync: include all content folders listed in [[README]]. Do not rely on agents to write `.obsidian/`.

Conflict-resolution is device-specific per vendor docs. The human must set it on desktop and mobile. Operator verifies by asking the human; Operator does not edit the setting file.

## What "synced" means

Local file existence is **not** Sync success.

After Sync is enrolled:

- Operator may use official UI status (green check, Sync log "Fully Synced") and, if the human enabled official CLI, `obsidian sync:status` against the **running** app.
- A human confirmation on a second device is required before claiming Sync success.

## Version history and restore

Restore and version history are human/official-surface operations:

- Obsidian Sync version history
- File Recovery core plugin (human)
- Official CLI `obsidian sync:history` / `obsidian sync:restore` only after human authentication in the running app, and never as a silent rewrite of an unresolved conflict

Agents do not restore over a conflicted note without a Curator conflict-disposition transaction.

## Recovery if broker/state disagrees

If receipts and filesystem diverge, treat filesystem + conflict copies as preserved evidence. Do not delete the extras. File a same-UID or Sync-drift finding.
