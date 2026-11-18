---
type: schema
created: 2026-09-16
pilot_days: 90
automatic_purge: false
pilot_start: null
---

# Retention Policy

Pilot length: **90 days** from the Operator-recorded scaffold timestamp (`pilot_start`, written into this note's frontmatter on first successful scaffold, not before).

During the pilot:

- There is **no automatic age-based purge**.
- Curator may authorize **non-destructive archive** when an artifact is superseded, no longer operationally active, or retained primarily as history. Record reason, replacement, source-owner notification, and date.
- Moving to `Trash/` is a **purge recommendation**, not deletion. Required concurrence: Curator **and** the responsible source profile or manager. If that owner is retired or unavailable, Orchestrator may provide the second organizational review. Security-sensitive material may require Security Auditor review.
- Permanent purge, deletion, or emptying `Trash/` is **human-only**. Neither Curator nor Operator may perform it. The broker has no delete/purge/empty-trash operation.
- After 90 days, Curator produces evidence-based retention recommendations from actual volume, retrieval, duplication, and maintenance cost. Do not invent permanent periods now.

## Archive record (required)

See Templates/archive-review.md. Archive without that record is invalid.

## Trash record (required)

See Templates/trash-recommendation.md. Trash-stage without both concurrences is invalid.

## Rollback vs deletion

Rollback of a failed create **moves** the new file to `Quarantine/rollback-<transaction_id>/`. It does not unlink. Quarantine is retained for the pilot.
