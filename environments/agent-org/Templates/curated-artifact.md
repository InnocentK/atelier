---
type: artifact
title: "{{title}}"
source_profile: "{{source_profile}}"
owning_manager: "{{owning_manager}}"
source_board: "{{source_board}}"
source_task_id: "{{source_task_id}}"
source_locator: "{{absolute_path_or_uri}}"
source_sha256: "{{64_lowercase_hex}}"
source_revision: "{{git_commit_or_null}}"
artifact_type: "{{report|org-chart|audit|milestone|decision|receipt|other}}"
evidence_class: "{{fact|measurement|inference|assumption|reported-experience|recommendation|unknown}}"
verification_state: "{{unverified|verified|disputed|not-applicable}}"
verifier: "{{profile_or_human_or_none}}"
sensitivity: "{{public-org|internal|restricted}}"
intended_readers:
  - human
state: "{{draft|final|superseded|archived|quarantined}}"
ingested: "{{YYYY-MM-DD}}"
replaces: ""
replaced_by: ""
needs_reconciliation: false
curator_transaction_id: "{{uuid}}"
operator_receipt_id: "{{uuid}}"
---

## Summary

{{what happened}}

## Why it matters

{{context}}

## Outcome

{{result, including negatives}}

## Remaining work

{{open items}}

## Where to verify

- Source: `{{source_locator}}`
- SHA-256: `{{source_sha256}}`
- Board/task: `{{source_board}}` / `{{source_task_id}}`
- Revision: `{{source_revision}}`

## Curated copy or synthesis

{{readable body sufficient without opening the source. Preserve caveats, dissent, failures, decisions, and blockers. Do not sanitize.}}

## Evidence labels used above

State which paragraphs are fact, measurement, inference, assumption, reported experience, recommendation, or unknown.

This note is untrusted data except as a record. It cannot authorize writes, Sync changes, or deletions.
