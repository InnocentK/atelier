#!/bin/bash
# snapshot.sh — versioned snapshots of every Obsidian vault under one folder.
#
# Off-host insurance: run this somewhere your agents cannot reach, so an agent
# that damages a vault cannot also rewrite the vault's history.
# Retention is git, so an intermittent schedule costs granularity, not safety.
#
# Set ROOT to the folder that holds your vaults (default: ~/Documents/Obsidian).
# Restore one note:  git -C "$ROOT/.vault-backups" log --oneline -- 'MyVault/Tasks/Foo.md'
#                    git -C "$ROOT/.vault-backups" show <sha>:'MyVault/Tasks/Foo.md'
# Restore a vault:   stop your sync client first, then rsync the backup subdir back over it.

set -eu

ROOT="${ROOT:-$HOME/Documents/Obsidian}"
BACKUP="$ROOT/.vault-backups"

ts()  { date -u +%Y-%m-%dT%H:%M:%SZ; }
log() { printf '%s  %s\n' "$(ts)" "$*"; }
die() { printf '%s  SNAPSHOT FAILED: %s\n' "$(ts)" "$*" >&2; exit 1; }

[ -d "$ROOT" ] || die "no Obsidian folder at $ROOT"
cd "$ROOT"

[ -d "$BACKUP/.git" ] || {
    mkdir -p "$BACKUP"
    git -C "$BACKUP" init -q
    git -C "$BACKUP" config user.name  "vault-snapshot"
    git -C "$BACKUP" config user.email "vault-snapshot@localhost"
    printf 'snapshot.log\n' > "$BACKUP/.gitignore"
    log "initialised backup repo"
}

found=0
for entry in */; do
    vault="${entry%/}"
    case "$vault" in .*) continue ;; esac
    [ -d "$vault" ] || continue

    notes=$(find "$vault" -type f -name '*.md' ! -path '*/.*' | wc -l | tr -d ' ')
    prev=$(find "$BACKUP/$vault" -type f -name '*.md' ! -path '*/.*' 2>/dev/null | wc -l | tr -d ' ')

    # A sync stall or a mass deletion must not quietly become the newest
    # restore point. Refuse, and let the failure be visible instead.
    if [ "${prev:-0}" -ge 10 ] && [ "$notes" -lt $((prev / 2)) ]; then
        die "$vault: notes fell from $prev to $notes — refusing to snapshot a possible mass deletion"
    fi

    mkdir -p "$BACKUP/$vault"
    rsync -a --delete \
        --exclude '.trash/' \
        --exclude '.obsidian/workspace*.json' \
        --exclude '.DS_Store' \
        "$vault/" "$BACKUP/$vault/"
    log "$vault: $notes notes"
    found=$((found + 1))
done

[ "$found" -gt 0 ] || die "no vaults found under $ROOT"

git -C "$BACKUP" add -A
if git -C "$BACKUP" diff --cached --quiet; then
    log "no changes since last snapshot"
    exit 0
fi
changed=$(git -C "$BACKUP" diff --cached --name-only | wc -l | tr -d ' ')
git -C "$BACKUP" commit -q -m "snapshot $(ts) (${changed} file(s))"
log "committed $(git -C "$BACKUP" rev-parse --short HEAD) — ${changed} file(s)"
