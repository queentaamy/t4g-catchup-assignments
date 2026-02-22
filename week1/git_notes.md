# Git Conflict Notes

## What is a git conflict?
A git conflict happens when Git cannot automatically merge changes because two branches modify the same part of a file. Git pauses the merge and asks you to resolve it manually.

## Steps to resolve a conflict
1. Run git status to see which files have conflicts.
2. Open the conflicted file.
3. Look for conflict markers (<<<<<<<, =======, >>>>>>>).
4. Decide which changes to keep.
5. Remove the conflict markers.
6. Save the file.
7. Run git add <file>.
8. Commit the resolved changes.
