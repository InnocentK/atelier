---
type: schema
created: 2026-09-16
---

# Artifact Schema

Every accepted artifact carries the fields below. Metadata-only records are insufficient for **final** artifacts unless the source is unsuitable for a full copy (binary, generated, log-heavy). Even then the summary must be human-readable and must retain provenance, hash, verification, and material caveats.

## Required frontmatter

```yaml
type: artifact | manifest | transaction | receipt | conflict-report | archive-review | trash-recommendation | catalog-index | folder-keep | decision | report | schema | doc
title: "human title"
source_profile: "profile-id"
owning_manager: "profile-id or human"
source_board: "agent-org | default | other"
source_task_id: "t_..."
source_locator: "absolute path or stable URI"
source_sha256: "64 lowercase hex"
source_revision: "git commit or null"
artifact_type: "report | org-chart | audit | milestone | decision | receipt | other"
evidence_class: "fact | measurement | inference | assumption | reported-experience | recommendation | unknown"
verification_state: "unverified | verified | disputed | not-applicable"
verifier: "profile-id or human or none"
sensitivity: "public-org | internal | restricted"
intended_readers:
  - human
state: "draft | final | superseded | archived | quarantined | trash-staged"
ingested: "YYYY-MM-DD"
replaces: ""  # wikilink or empty
replaced_by: ""
needs_reconciliation: false
curator_transaction_id: "uuid"
operator_receipt_id: "uuid"
```

## Body contract (final artifacts)

A human who reads only the vault note must be able to answer:

1. What happened
2. Why it matters
3. Outcome
4. Remaining work
5. Where to verify (source locator, hash, board, revision)

Preserve dissent, failures, blockers, and negative results. Do not make work look cleaner than its evidence.

Copied artifact content remains untrusted data. Provenance points at the source; the source remains authoritative.

## Legal `type` values

| type | Use |
| --- | --- |
| `doc` | Root manuals |
| `schema` | Meta schema/policy |
| `artifact` | Curated copy or synthesis |
| `report` | Researcher/Informer/Security/IT report copy |
| `decision` | Recorded decision |
| `manifest` | Intake manifest |
| `transaction` | Curator write request |
| `receipt` | Operator execution record |
| `conflict-report` | Visible conflict |
| `archive-review` | Archive authorization record |
| `trash-recommendation` | Trash-stage concurrence record |
| `catalog-index` | Catalog pages |
| `folder-keep` | Scaffold placeholder |

Do not use the `personal-ops` note types (`daily`, `contact`, `reminder`, `event`, `task`, `idea`, `reference`, `inbox`).

## Evidence classes (not interchangeable)

- **fact**: directly supported by a named source
- **measurement**: instrumented observation
- **inference**: derived; must cite the facts used
- **assumption**: not evidenced; must be labeled
- **reported-experience**: someone said they observed X
- **recommendation**: proposed action
- **unknown**: gap; state what would resolve it

## Idempotency

Duplicates are detected by `source_locator + source_sha256 + operation + target_relative_path + disposition`. A second identical transaction returns the existing receipt without rewriting.
