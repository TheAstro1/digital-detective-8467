# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use the command line to inspect the current folder, safely create and manage practice files, compare command options, understand pipes, and explain package managers.

## 2. Work completed
### Basic operations
| Operation | Command | What it does / what to observe |
|---|---|---|
| Current-directory display | `pwd` | Prints the absolute path of the current working directory. |
| Directory listing | `ls` | Lists visible names in the current folder. |
| Detailed listing | `ls -l` | Shows a long listing, including permissions, owner, size, and modification time. |
| Change to parent | `cd ..` | Moves the shell's working directory one level up; `pwd` then shows the new location. |
| Create a practice folder | `mkdir terminal-practice` | Creates a directory in the current location. |
| Create an empty file | `touch terminal-practice/notes.txt` | Creates the file if absent; if present, updates its modification time. |
| Copy a file | `cp terminal-practice/notes.txt terminal-practice/notes-copy.txt` | Creates a separate copy while leaving the source in place. |
| Rename / move a file | `mv terminal-practice/notes-copy.txt terminal-practice/backup.txt` | Moves the file to another path; using a new name in the same folder renames it. |
| Display file contents | `cat terminal-practice/notes.txt` | Prints the text file's contents. |

### Append and backup practice
Run these from the repository root. They only write inside `terminal-practice/`:

```bash
mkdir -p terminal-practice
printf '%s\n' 'First line' > terminal-practice/notes.txt
printf '%s\n' 'Second line' >> terminal-practice/notes.txt
cat terminal-practice/notes.txt
cp terminal-practice/notes.txt terminal-practice/notes-backup.txt
mv terminal-practice/notes-backup.txt terminal-practice/notes-archive.txt
```

`>` creates or replaces a file's contents; `>>` appends text without replacing existing lines. Copying leaves the original in place, while moving relocates or renames the file. `pwd` identifies where relative paths refer, and a directory listing helps locate files and inspect their names.

### Flags and pipes
| Command | What changes |
|---|---|
| `ls` | Basic listing. |
| `ls -lah` | Long format (`-l`), includes hidden names (`-a`), and uses human-readable sizes (`-h`). |
| `ls -lah \| head -n 5` | Sends the listing to `head`, which prints its first five lines. |

The pipe (`|`) connects commands: the first command writes output, and the next command reads that output as input. Hidden-file names or detailed listings can contain private information; inspect locally and redact before sharing.

### Package managers
A package manager keeps track of software packages and can help install, update, and remove them with consistent commands. On macOS, if Homebrew is already installed, `brew --version` checks it and `brew list` displays managed packages. This assignment does not require installing or uninstalling anything.

## 3. Commands / tools used
`pwd`, `ls`, `cd`, `mkdir`, `touch`, `printf`, `cat`, `cp`, `mv`, `head`, the pipe operator (`|`), and optionally `brew --version` / `brew list`. Use only the commands you actually ran in your own final notes.

## 4. My understanding
The shell keeps a current working directory, so a relative path is interpreted from that location. Redirection controls where command output goes, while a pipe passes output to another command. Flags modify a command's behavior. Practising inside a dedicated folder makes file experiments easier to inspect and keeps them separate from system files.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- This README contains command examples and explanations.
- `terminal-practice/` created during the practical exercise.

## 8. Commit details
- Commit message: `mission-02: Completed Terminal and file management mission`
