# Tools

## snapshot.sh

Takes a versioned snapshot of every vault under one folder into a git
repository beside them. Run it on a schedule from a machine or account your
agents cannot reach, so an agent that damages a vault cannot also rewrite the
vault's history.

```sh
ROOT="$HOME/Documents/Obsidian" ./snapshot.sh
```

It refuses to record a bad state: it stops if the folder is missing, if no
vaults are found, or if a vault's note count has fallen by more than half
since the last snapshot. A sync stall or a mass deletion must not quietly
become the newest restore point.

To roll a whole vault back, stop your sync client first, then copy the backup
subdirectory over the vault. Restoring underneath a live sync client produces
a storm of conflicts.
