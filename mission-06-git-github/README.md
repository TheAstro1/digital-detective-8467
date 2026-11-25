# Mission 6 — Git and GitHub

## 1. Task / objective
Explain Git's basic workflow, create and publish a branch, open a Pull Request on GitHub, and define common Git commands.

## 2. Work completed
### Basic workflow
| Git operation | What it does |
|---|---|
| Check status: `git status` | Shows the current branch and working-tree changes. |
| Stage selected work: `git add README.md` | Selects a change for the next commit; it remains a local change. |
| Commit: `git commit -m "Describe the change"` | Records the staged snapshot in local history. |
| View history: `git log --oneline` | Displays concise recent commits. |

Staging is a reviewable selection of changes for the next snapshot; committing records that selected snapshot in the repository's history. A staged change is not yet a commit, and a local commit is not automatically published to GitHub.


### Git command glossary
| Operation | Command example | Meaning |
|---|---|---|
| Initialize | `git init` | Start version tracking in the current folder. |
| Check status | `git status` | Inspect changes and staging state. |
| Stage selected changes | `git add path` | Select paths for the next commit. |
| Commit | `git commit -m "message"` | Save staged changes in local history. |
| View history | `git log --oneline` | Review existing commits. |
| Create/list branches | `git switch -c name` / `git branch` | Create and switch to a branch / list branches. |
| Switch branches | `git switch main` | Move the working tree to another branch. |
| Publish changes | `git push` | Send local commits to a remote repository. |
| Retrieve remote changes | `git pull` | Fetch and integrate changes from a remote branch. |

## 3. Commands / tools used
The examples use `git status`, `git add`, `git commit`, `git log`, `git switch`, `git branch`, `git push`, and `git pull`, plus the GitHub web interface for Pull Request review. Only report operations you personally performed.

## 4. My understanding
Git records project history locally. The staging area lets a contributor choose exactly what belongs in the next commit. Branches keep independent work separate, and a Pull Request provides a review and discussion step before proposed changes are integrated. Pushing publishes local commits; pulling brings remote changes into the local branch.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- This README — Git explanations and a branch/PR walkthrough.


## 8. Commit details
- Commit message: `mission-06: Complete Git and GitHub collaboration mission`
