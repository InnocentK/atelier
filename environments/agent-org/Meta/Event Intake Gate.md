---
type: schema
created: 2026-09-16
status: disabled
---

# Event Intake Gate

`status: disabled`

Event-driven publication from task board completion, cron, filesystem watchers, or gateway events is **off** until the manual pilot acceptance matrix passes.

While disabled:

- Operator must refuse any transaction whose `approval.basis` is `event` or `task-completion-hook`.
- The only accepted delivery channel is `task-board-attachment` (manual Curator/human approval). Filesystem drops, hooks, cron, and gateway events are unbound channels.
- Curator must not issue transactions solely because a task completed.
- Ordinary profiles continue to submit manifests through task board for **manual** Curator review.

Enabling this gate is a human decision after:

scaffold, Sync, secret refusal, duplicate handling, human-edit reconciliation, archive, Trash staging, conflict behavior, search, and restore tests all pass.

No agent may flip `status` to `enabled` as part of scaffold.
