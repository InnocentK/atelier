---
type: schema
created: 2026-09-16
fail_closed: true
---

# Sensitivity Policy

## Classes

| sensitivity | Meaning | Default readers |
| --- | --- | --- |
| `public-org` | Organizationally shareable inside Agent Org | human + all registered profiles |
| `internal` | Ordinary org work, not for extra-vault publication | human + relevant managers |
| `restricted` | Security/IT evidence, hostnames, architecture | human, security-auditor, curator, relevant operator/technician |
| *(reject)* | Secret or forbidden source | none — refuse, do not ingest |

There is no `secret` class in this vault. Secret-bearing material is **rejected**, not classified downward.

## Fail closed

Secret and sensitivity scans that error, timeout, or cannot complete **reject** the transaction. Do not publish.

Never log matched values, snippets, or capturing groups. Log only: `rule_id`, `source_locator` (path), `outcome=refused`.

Hashes that are usable as authentication (password hashes, signing secrets, API token hashes) are forbidden, even if "already hashed".

## Forbidden sources (reject before body read)

Positive allowlist is `broker/source-allowlist.md`. Everything else is refused. Category-level refusal still applies to allowlisted prefixes:

- Raw agent sessions and transcripts
- Private personal content and personal vaults
- Personal operations notes (a separate domain)
- Unredacted logs (`logs/`, `agent.log`, `errors.log`, `*.log`)
- Caches, virtual environments, `node_modules`, `__pycache__`
- Credential files, `.env`, private keys, `ssh/` material, keychains, tokens, cookies, JWTs
- Broad secret-bearing configuration (any profile/host JSON/TOML/YAML dump, agent runtime configuration files)
- Authentication verifiers/hashes (`password_hash`, bcrypt/argon2/scrypt strings used as verifiers)
- Unsupported binaries as source bodies

Do not rely on case-sensitive substring denylists. Identity uses `O_NOFOLLOW` and filesystem-appropriate comparison.

## Forbidden vault content

No passwords, tokens, private keys, account numbers, recovery material, verification codes, or authentication hashes.

`Operations/Secrets-Metadata/` may record only: secret *exists*, owning profile, rotation due date, pointer to the real store (1Password/Bitwarden item name without value).

## Redaction in curated copies

If a source is otherwise eligible but contains a secret substring, **do not ingest**. Return to the source owner for a redacted revision. Curator does not silently strip secrets and publish the rest (too easy to miss a second secret). Exception: Security Auditor reports that already state values were not recorded and contain only redaction markers may be ingested as `restricted` after a fresh scan passes.
