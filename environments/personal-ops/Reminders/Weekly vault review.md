---
type: reminder
remind: 2026-01-05
repeat: weekly on Monday
status: active
created: 2026-01-01
---

The standing trigger for vault maintenance — Inbox drainage and Archive sweeps must not depend on anyone remembering them. Whichever agent is active when this fires:

1. Run the [[AGENTS#Health check]]; fix mechanical violations and log the fixes.
2. Drain `Inbox/`: retype and move every item per [[AGENTS#Where does it go?]]; raise unclassifiable ones as NEEDS-INPUT.
3. Sweep stragglers into `Archive/`: done or dropped tasks, fired one-shot reminders, events whose `date`/`end` is before today.
4. Scan the past week's `Daily/` notes for unanswered `NEEDS-INPUT:` lines and re-surface them to the owner.
5. Glance at `Ideas/`: archive any whose status changed; re-surface `open` ideas whose `revisit` date has passed, or that lack one and are a month old. When the owner defers a decision, set that idea's `revisit` instead of letting it nag.
6. If `Trash/` is non-empty, ensure a [[Review the Trash folder]] task exists — `open`, due tomorrow, body listing the current contents. Create it, or update the existing one, per search-before-create.
7. Advance `remind` to the next Monday and log a one-line summary in today's daily note.
