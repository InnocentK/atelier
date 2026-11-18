---
type: conflict-report
title: "Conflict: {{note basename}}"
state: needs-reconciliation
needs_reconciliation: true
sensitivity: "{{internal|restricted}}"
canonical_relative_path: "{{path}}"
canonical_sha256: "{{64_hex}}"
conflict_copy_relative_path: "{{path or empty}}"
conflict_copy_sha256: "{{64_hex or empty}}"
human_edit_detected: true
source_sha256: "{{expected source if any}}"
transaction_id_blocked: "{{uuid or empty}}"
reported_at: "{{ISO-8601}}"
---

## Versions left in place

Do not delete or merge these until a Curator conflict-disposition transaction plus any required human decision.

1. Canonical: `{{canonical_relative_path}}` SHA-256 `{{canonical_sha256}}`
2. Conflict copy or human-divergent bytes: `{{conflict_copy_relative_path}}` SHA-256 `{{conflict_copy_sha256}}`

## Overlap description

{{what both sides changed. No secret values.}}

## Requested decision

- merge-preserving-both (only if Curator confirms non-overlap after reading both)
- keep-canonical
- keep-conflict-copy
- human-rewrite

Operator must not choose.
