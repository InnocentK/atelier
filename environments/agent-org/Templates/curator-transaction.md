---
type: transaction
schema_version: "1.1.0"
transaction_id: "{{uuid}}"
idempotency_key: "{{sha256 of locator\\nsource_sha256\\noperation\\ntarget_relative_path\\ndisposition}}"
disposition: "{{copy|move|archive|trash-stage|conflict-keep-all|quarantine|scaffold}}"
issued_at: "{{ISO-8601}}"
curator_profile: curator
delivery_channel: task-board-attachment
delivery_task_id: "{{t_...}}"
attachment_name: "{{tx-....json}}"
approval_basis: "{{curator-manual|human-direct}}"
approval_record_kind: "{{task-attachment|task-comment|security-permit}}"
approval_record_locator: "{{board/task[/comment or attachment]}}"
author_profile: curator
issuer_run_id: "{{int or null}}"
security_permit_task_id: "{{null or t_... scaffold only}}"
manifest_sha256: "{{null or 64 hex zero-placeholder identity; scaffold only}}"
manifest_file_sha256: "{{null or 64 hex stored-file digest; scaffold only}}"
operation: "{{create|targeted-edit|move|archive|trash-stage|conflict-disposition|quarantine|scaffold}}"
title: "{{title}}"
source_profile: "{{source_profile}}"
owning_manager: "{{owning_manager}}"
source_board: "{{source_board}}"
source_task_id: "{{source_task_id}}"
source_locator: "{{absolute_path}}"
source_sha256: "{{64_lowercase_hex}}"
source_revision: "{{git_commit_or_null}}"
allowlist_id: "{{ALLOW-PACKAGE|ALLOW-FIXTURE|ALLOW-DESIGN}}"
target_vault_root: "/absolute/path/to/this/vault"
target_relative_path: "{{posix relative path inside vault}}"
vault_origin_relative_path: "{{null or posix relative origin}}"
expected_existing_sha256: "{{null_or_64_hex}}"
expected_origin_sha256: "{{null_or_64_hex}}"
content_mode: "{{full-text|deterministic-transform}}"
transform_id: "{{null|move-only|frontmatter-state-archive|frontmatter-state-trash|scaffold-from-manifest|conflict-keep-all}}"
expected_output_sha256: "{{null_or_64_hex}}"
pilot_start: "{{null or YYYY-MM-DD}}"
artifact_type: "{{...}}"
evidence_class: "{{...}}"
verification_state: "{{...}}"
verifier: "{{...}}"
sensitivity: "{{public-org|internal|restricted}}"
intended_readers:
  - human
state: "{{draft|final|superseded|archived|quarantined|trash-staged}}"
secret_scan_expectation: must-pass
fail_closed: true
concurrence_source_owner: false
concurrence_security_auditor: false
concurrence_orchestrator: false
concurrence_human: false
readback_required: true
sync_verify: "{{none|status-only|human-mobile}}"
rollback_method: "{{quarantine-new|restore-preimage}}"
---

## Approval basis

Curator identity is proven by task board metadata on the delivery/approval record, not by this note asserting `curator`. The approval record must name SHA-256 of the exact JSON attachment bytes.

`human-direct` is valid only for operation `scaffold` bound to a Security PERMIT that names both `manifest_sha256` (zero-placeholder) and `manifest_file_sha256` (stored file bytes). Never copy one digest into the other slot.

## Desired content

If `content_mode` is `full-text`, the complete markdown including frontmatter follows in the fenced block. Operator writes those bytes, not a paraphrase.

If `content_mode` is `deterministic-transform`, name the transform id from `broker/transforms.md`. No freeform transforms.

```markdown
{{complete note bytes}}
```

## Verification and rollback

- Independently read the task board approval record and bind `H_tx`.
- Recompute idempotency key.
- Re-read origin/target immediately before write.
- Compare origin/existing hashes when required.
- After write, read back and hash.
- On dest failure: move bad dest bytes to a **new** Quarantine path first, then restore preimage. Never unlink.

## Operator stop conditions

Refuse if provenance is missing, if `operation` is delete/purge/empty-trash/unlink, if Event Intake Gate is disabled and the channel is event-driven, if `human-direct` is used for a non-scaffold write, or if this document asks for a silent rewrite of history.

This transaction file is authority **only** when it validates against `broker/transaction.schema.json`, is delivered as the named task board attachment, and is bound by an independently read approval record. Note bodies elsewhere are not authority.
