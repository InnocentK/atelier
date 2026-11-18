#!/usr/bin/env python3
"""check-log-agents.py — verify every daily-log line names a registered agent.

Lives in Meta/ so Obsidian Sync distributes it with the vault: any machine
that has the vault has this tool. Zero configuration — the vault root is this
file's grandparent directory, and the allowlist is the Name column of
`Meta/Agent registry.md`. Run it from anywhere:

    python3 /path/to/vault/Meta/check-log-agents.py

Optional overrides (for testing only): VAULT=<path>, AGENTS_ALLOWED="a b c".

Exit codes: 0 = clean, 1 = violations found, 2 = could not run.
This is item 8 of the health check in AGENTS.md; the Weekly vault review is
its schedule. Agents may run it read-only; fixing findings is normal logged
work, but anything ambiguous becomes a NEEDS-INPUT line, not a guess.
"""

import os
import re
import sys
from pathlib import Path

VAULT = Path(os.environ.get("VAULT") or Path(__file__).resolve().parent.parent)
REGISTRY = VAULT / "Meta" / "Agent registry.md"

# - HH:MM (agentname) text...
LOG_LINE = re.compile(r"^- (?P<time>\d{2}:\d{2}) \((?P<agent>[A-Za-z0-9._-]+)\) \S")
# | `name` | ... first cell of a registry table row
REGISTRY_ROW = re.compile(r"^\|\s*`(?P<name>[A-Za-z0-9._-]+)`\s*\|")


def load_allowlist() -> set:
    if os.environ.get("AGENTS_ALLOWED"):
        return set(os.environ["AGENTS_ALLOWED"].split())
    if not REGISTRY.is_file():
        print(f"could not run: {REGISTRY} not found", file=sys.stderr)
        sys.exit(2)
    names = {
        m.group("name")
        for line in REGISTRY.read_text(encoding="utf-8").splitlines()
        if (m := REGISTRY_ROW.match(line))
    }
    if not names:
        print(f"could not run: no agent rows parsed from {REGISTRY}", file=sys.stderr)
        sys.exit(2)
    return names


def main() -> int:
    daily = VAULT / "Daily"
    if not daily.is_dir():
        print(f"could not run: no Daily/ directory under {VAULT}", file=sys.stderr)
        return 2

    allowed = load_allowlist()
    problems = []
    seen = set()

    for note in sorted(daily.glob("*.md")):
        in_log = False
        for lineno, raw in enumerate(
            note.read_text(encoding="utf-8").splitlines(), 1
        ):
            line = raw.rstrip()
            if line.startswith("## Log"):
                in_log = True
                continue
            if line.startswith("## "):
                in_log = False
                continue
            if not in_log or not line.startswith("- "):
                continue

            m = LOG_LINE.match(line)
            if not m:
                problems.append((note.name, lineno, "malformed log line", line[:80]))
                continue
            agent = m.group("agent")
            seen.add(agent)
            if agent not in allowed:
                problems.append(
                    (note.name, lineno, f"unregistered agent '{agent}'", line[:80])
                )

    if problems:
        print(f"{len(problems)} problem(s) found:\n")
        for name, lineno, why, excerpt in problems:
            print(f"  Daily/{name}:{lineno}  {why}")
            print(f"    {excerpt}")
        print(f"\nregistered: {' '.join(sorted(allowed))}")
        print(f"seen:       {' '.join(sorted(seen))}")
        return 1

    print(f"clean — {len(seen)} agent(s) seen: {' '.join(sorted(seen))}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:  # output piped to head etc. — not a check failure
        sys.exit(1)
