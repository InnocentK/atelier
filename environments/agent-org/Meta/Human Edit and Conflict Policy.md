---
type: schema
created: 2026-09-16
---

# Human Edit and Conflict Policy

Human desktop and mobile edits are **valid concurrent input**, not violations. Agents are the dominant writers but never exclusive.

## Before every Operator edit

1. Re-read the exact target bytes from disk.
2. Compute SHA-256.
3. Compare to `expected_existing_sha256` in the transaction (required for targeted-edit, move, archive, trash-stage).
4. If mismatch: **stale target**. Stop. Do not write. Return hashes and paths to Curator.

## Non-overlapping changes

If the human edited a region the transaction does not touch:

- Operator does not guess a merge.
- Return both the current target hash and the intended patch to Curator.
- Curator issues a new transaction whose `full_text` preserves both the human meaning and the intended agent change.
- Attribution: keep human-authored sentences; do not restyle them.

## Overlapping or ambiguous changes

- Leave **all** versions in place, including official Sync conflict copies:
  `original-note-name (Conflicted copy device-name YYYYMMDDHHMM).md`
- Write a `conflict-report`.
- Mark the artifact `needs_reconciliation: true`.
- Block the transaction. No overwrite, no auto-merge, no Trash of the husk until Curator + human disposition.

## Official Sync behavior we rely on

Vendor docs (Obsidian 1.9.7+): conflict resolution is device-specific. **Automatically merge** uses diff-match-patch on Markdown and can combine edits without a visible extra file. This vault requires **Create conflict file** so conflicts cannot be silently lost.

If a device is found on auto-merge, treat that as a pilot failure for conflict tests until the human sets Create conflict file on that device.

## Same-UID / non-Sync mystery edits

If a file changes without a receipt and without a conflict copy, record a same-UID detection finding. Do not revert it automatically; it may be a legitimate human edit that did not yet sync.
