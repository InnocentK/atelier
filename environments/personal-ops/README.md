---
type: doc
created: 2026-08-06
---

# Personal Ops

Personal Ops is an **agent-managed operations vault**. AI agents do most of the reading and writing here on the owner's behalf: reminders, calendar-style planning, tasks, contacts, and daily operational notes.

It is deliberately **not** a general-purpose notes vault or a "second brain" — other vaults exist (or will) for that. This vault trades expressive freedom for a small set of note types with predictable names, locations, and properties, so humans can navigate it and agents can automate against it without guesswork. Freeform journaling, knowledge notes, and research don't belong here; if something like that lands here anyway, it sits in `Inbox/` until the owner rehomes it. The vault also never holds secrets — no passwords, credentials, or account numbers, period; genuinely sensitive data belongs in a separate, locally guarded vault.

Three root files define the vault: [[README]] (this file) describes structure and conventions, [[AGENTS]] is the operating manual every AI agent must follow, and [[CLAUDE]] adds Claude-specific notes.

## Layout

| Folder | Contains |
| --- | --- |
| `Calendar/` | Scheduled events and appointments — one note per event |
| `Contacts/` | People and organizations — one note per contact |
| `Daily/` | One note per day: the day's notes and the agent activity log |
| `Ideas/` | Proposals and thoughts to revisit — the owner's ideas and agent suggestions, tracked to a decision |
| `Inbox/` | Temporary triage zone — captures awaiting review and filing, never long-term storage |
| `Meta/Templates/` | Skeleton templates for each note type |
| `Reference/` | Durable operational facts — addresses, institutions, products, history — one note per subject |
| `Reminders/` | Date-triggered nudges — one note per reminder |
| `Tasks/` | Actionable work items tracked to completion — one note per task |
| `Trash/` | Staged for deletion by agents; only the owner empties it |
| `Archive/` | Finished/expired items in subfolders mirroring the active folders: `Archive/Tasks/`, `Archive/Reminders/`, `Archive/Calendar/` |

`.obsidian/` is app configuration, not content — agents never touch it. Folders that aren't needed yet (e.g. `Archive/` subfolders) are created on first use; note that Obsidian Sync does not propagate empty folders to other devices.

## Naming

Dates are always **YYYY-MM-DD** — in filenames and in property values. Times are 24-hour `HH:MM`. Filenames are plain natural language using letters, digits, spaces, and hyphens (avoid `# ^ [ ] | / \ :`), and must be unique across the vault so wikilinks resolve unambiguously.

| Note | Filename pattern | Example |
| --- | --- | --- |
| Daily note | `YYYY-MM-DD` | `Daily/2026-08-06.md` |
| Event | `YYYY-MM-DD Short description` (date = start date) | `Calendar/2026-08-20 Dentist appointment.md` |
| One-shot reminder | `YYYY-MM-DD Short description` (date = trigger date) | `Reminders/2026-09-01 Renew car insurance.md` |
| Recurring reminder | Descriptive name, no date | `Reminders/Weekly vault review.md` |
| Task | Short imperative name, no date — dates live in properties | `Tasks/Book flights.md` |
| Contact | The person's or organization's name | `Contacts/Jane Doe.md` |
| Idea | Short descriptive name, no date | `Ideas/Split into multiple vaults.md` |
| Reference | Short subject name, no date | `Reference/Credit cards.md` |

Date-prefixed folders read as a chronological queue when sorted by name — that's the point. Notes never repeat the filename as an `# H1` (Obsidian already shows the filename as the title); bodies start directly with content or `##` sections.

## Time and timezone

All dates and times in this vault are assumed to be **Your/Timezone** unless a note explicitly says otherwise. Time values must use 24-hour format `"HH:MM"` (quoted in YAML) — no other time format is used. If this ever changes, the new timezone gets updated here and in [[AGENTS#Time and timezone]], and the change is treated as part of the vault's conventions.

Filenames and date-type properties always use full `YYYY-MM-DD`. Dates in note bodies — reference histories especially — may be partial, down to a minimum of a year (`2024`, `2024-03`); prefix estimates with `~` (`~2024`); write `unknown` rather than guessing, and fill it in if the real date ever surfaces. When a date-type *property* is an approximation (an estimated birthday, say), it still carries a full plausible `YYYY-MM-DD`, and the field name sits in that note's `estimated:` list property until corrected.

## Properties (frontmatter)

Every note carries YAML frontmatter declaring at least its `type`: `daily`, `event`, `reminder`, `task`, `contact`, `idea`, `reference`, `inbox`, or `doc`. Tasks, reminders, events, contacts, ideas, and reference notes also carry an optional single-value `area` (`work`, `personal`, `family`, or `homelab`) for slicing items by life area. Each type's full property set is defined by its skeleton in `Meta/Templates/`, with semantics in [[AGENTS#Note types]]. Properties are what make the vault machine-readable — filterable with core Bases, no community plugins required.

## Linking

Use `[[wikilinks]]` liberally; they power backlinks, graph view, and navigation:

- Mention a person → link the contact: `[[Jane Doe]]`.
- Reference a day → link its daily note: `[[2026-08-12]]`, even if it doesn't exist yet — unresolved links are fine and become hubs later.
- Related notes link each other: a task ↔ the event it prepares for, an event → its attendees.
- `[[Note#Heading]]` and `[[Note|display text]]` where they help; contacts can declare `aliases` so nicknames resolve.
- Inside properties, wikilinks must be quoted: `attendees: ["[[Jane Doe]]"]`.

Links resolve by filename, so **moving** a note (e.g. into `Archive/`) is safe, but **renaming** one outside Obsidian breaks inbound links — see the rules in [[AGENTS]].

## Tags

Mostly unnecessary here: folders, `type`, and status properties already encode what tags would — never duplicate those as tags. Optional lowercase-kebab tags (`#travel`, `#health`) may mark cross-cutting themes.

## Archive, don't delete

Active folders hold only current items; when something finishes it moves — it is never deleted. The mirrored subfolders in use are exactly these four, each created on first use: completed or dropped tasks → `Archive/Tasks/`, fired one-shot reminders → `Archive/Reminders/`, past events (`date` — or `end` — before today) → `Archive/Calendar/`, decided ideas → `Archive/Ideas/`. Any new `Archive/` subfolder must follow the same name-mirroring pattern and is added intentionally, as a conventions change — not ad hoc. Disposal is separate from archiving: root-level `Trash/` holds anything an agent stages for deletion (resolved sync-conflict husks, items the owner asked removed), and emptying it is the owner's act alone — the weekly review flags it whenever it's non-empty. Daily notes stay in `Daily/`; past years can move to `Archive/Daily/` someday if the folder feels crowded. A standing [[Weekly vault review]] reminder is the explicit trigger for the archive sweep and `Inbox/` triage, so vault hygiene never depends on anyone remembering.

## Obsidian setup

The vault is intentionally kept close to Obsidian's default behavior so it's equally predictable from the app and from the CLI: core features only (Properties, Daily Notes, Templates, Bases, Sync), no community plugins, plain `[[wikilinks]]` with no link-rewriting machinery on top, and properties used conservatively — `type`, status, and the date fields the templates define, nothing speculative. Two one-time settings make the app match these conventions:

- **Settings → Daily notes** → New file location: `Daily` (date format stays `YYYY-MM-DD`).
- **Settings → Templates** → Template folder location: `Meta/Templates`.

A saved Base at `Meta/Ops.base` provides the live operational views — open tasks, active reminders, upcoming events, inbox by capture age, open ideas, and a contacts directory — all driven by properties, with `Archive/`, `Meta/`, and `Trash/` excluded from every view.
