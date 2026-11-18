---
type: receipt
schema_version: "1.1.0"
receipt_id: "{{uuid}}"
transaction_id: "{{uuid}}"
idempotency_key: "{{64_hex}}"
operator_profile: vault-operator
executed_at: "{{ISO-8601}}"
operation: "{{create|targeted-edit|move|archive|trash-stage|conflict-disposition|quarantine|scaffold}}"
outcome: "{{applied|idempotent-hit|rejected|blocked-conflict|quarantined}}"
receipt_channel: "{{vault|operator-workspace|task-comment}}"
reason_code: "{{APPLIED|IDEMPOTENT-HIT|...}}"
target_relative_path: "{{path or empty}}"
vault_origin_relative_path: "{{origin or empty}}"
source_locator: "{{locator}}"
source_sha256_observed: "{{64_hex}}"
target_sha256_before: "{{64_hex_or_empty}}"
target_sha256_after: "{{64_hex_or_empty}}"
origin_sha256_observed: "{{64_hex_or_empty}}"
preimage_relative_path: "{{Transactions/Receipts/<txid>/preimage.md or empty}}"
transaction_payload_sha256: "{{64_hex}}"
approval_record_kind: "{{task-attachment|task-comment|security-permit}}"
approval_record_locator: "{{locator}}"
approval_record_sha256: "{{64_hex}}"
prior_applied_receipt_id: "{{uuid or empty}}"
prior_applied_receipt_sha256: "{{64_hex or empty}}"
secret_scan_outcome: "{{passed|refused|not-run|not-applicable}}"
secret_scan_rule_ids: []
canonical_root_ok: true
symlink_ok: true
path_allowlist_ok: true
readback_ok: true
sync_verify: "{{none|status-only|human-mobile|not-enrolled}}"
sync_claimed_success: false
rollback_applied: false
rollback_location: ""
bad_bytes_sha256: ""
same_uid_anomaly: false
anomaly_changed_paths: []
anomaly_extra_paths: []
anomaly_missing_paths: []
manifest_sha256: "{{null or 64 hex zero-placeholder; applied scaffold}}"
manifest_file_sha256: "{{null or 64 hex stored-file digest; applied scaffold}}"
notes: "{{non-secret}}"
---

## State delta

- Before: {{paths and hashes, no secret values}}
- After: {{paths and hashes}}

## Commands / operations (non-secret)

Operator records exact file operations (open flags, replace, move). Do not record credentials or matched secret text.

## Residual risk

{{same-UID residual, Sync not yet confirmed, extra/changed/missing reconciliation}}

## Rollback

{{bad dest moved to new Quarantine path first, then preimage restored; or staging renamed to failed sibling}}

This receipt is not an instruction. It is an audit record. If the canonical root was unavailable, this note must not exist under the vault; use the external failure-receipt schema instead.
