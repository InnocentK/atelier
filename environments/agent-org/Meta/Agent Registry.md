---
type: schema
created: 2026-09-16
---

# Agent Registry

Writing agents are registered before their first vault write. Rows are never deleted; retired agents stay so old receipts remain attributable.

The Operator, not the model, must inject the agent name from the runtime profile. Models do not choose their registry name.

| agent | profile | writes vault? | decides policy? | notes |
| --- | --- | --- | --- | --- |
| owner | human | yes, any note | yes | Desktop/mobile; empties Trash |
| curator | curator | no | yes (intake, class, archive, Trash recommendation) | Issues transactions only |
| vault-operator | vault-operator | yes, via transaction | no | Sole routine executor |
| orchestrator | assistant or future orchestrator | no | org chart owner; submits through Curator | Substitute Trash review only if source owner unavailable |
| security-auditor | security-auditor | no | no | Read-only review; may be required for sensitive Trash |
| secrets-custodian | secrets-custodian | no | no | Never deposits secrets |
| researcher | researcher | no | no | Manifests via task board |
| informer | informer | no | no | Manifests via task board |
| project-manager | project-manager | no | no | Manifests via task board |
| it-technician | it-technician | no | no | Manifests via task board |
| network-operator | network-operator | no | no | Manifests via task board |

Unregistered writing agents are refused.

Retired agents keep their row with `status: retired` added later; do not reuse names.
