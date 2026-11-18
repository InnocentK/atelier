---
type: trash-recommendation
title: "Trash-stage: {{artifact title}}"
artifact_relative_path: "{{path}}"
artifact_sha256: "{{64_hex}}"
trash_destination: "Trash/{{basename}}"
reason: "{{why purge is recommended}}"
curator_concurred: true
source_owner_profile: "{{profile}}"
source_owner_concurred: false
orchestrator_substitute: false
orchestrator_reason_if_substitute: ""
security_auditor_required: false
security_auditor_concurred: false
human_purge_authorized: false
date: "{{YYYY-MM-DD}}"
transaction_id: "{{uuid}}"
---

## Concurrence

Trash-stage requires Curator **and** source owner/manager. Orchestrator may substitute **only** if that owner is retired or unavailable; record why. Security-sensitive material additionally requires Security Auditor review.

Permanent deletion remains human-only. This record does **not** authorize emptying `Trash/`.

## Why not Archive

{{distinction}}
