# Mission 3 — Understand the operating system

## 1. Task / objective
Explore operating-system information, running processes, available storage, paths, and file permissions; explain the main responsibilities of an operating system.

## 2. Work completed
### System information and process observations
| Information | What it tells you | Privacy-safe observation |
|---|---|---|
| Operating system | Identifies the operating-system family and version. | ProductName: macOS; ProductVersion: 27.2.1; BuildVersion: 26B131 |
| Current account | Prints the account name used by the current shell. | `[redacted]` |
| Available storage | Reports used and available space for the filesystem containing the current directory. | approx. 25%. |
| Activity snapshot | Shows a snapshot of processes and resource use. | - |
| Process list | Lists processes; the PID column is each process's identifier. | - |

A process is a running instance of a program. Its process identifier (PID) is a number the operating system uses to distinguish and manage that running instance. Examples could include a browser process and a text editor, but the actual list depends on what is open.

### Paths and permissions
An absolute path starts at the filesystem root and identifies a location independently of the current folder, for example `/absolute/path/to/repository/mission-03-operating-system/`. A relative path is interpreted from the current folder, for example `mission-03-operating-system/README.md` when run from the repository root.

Use `pwd` to inspect the current location and `ls -l mission-03-operating-system/README.md` to inspect a file's permissions. In a mode such as `-rw-r--r--`, the first three permission letters after the file-type character (`rw-`) apply to the owner: read (`r`) and write (`w`) are allowed; execute (`x`) is not. Permission letters on a directory have related but distinct meaning: `x` permits traversal/search.

| Permission | Meaning | Example |
|---|---|---|
| `r` — read | Read file contents; on a directory, list names. | Open a text file. |
| `w` — write | Change file contents; on a directory, create or remove entries when other conditions allow. | Edit a document. |
| `x` — execute | Run a file; on a directory, traverse/search it. | Run an executable script. |


### Operating-system responsibilities
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts, schedules, and ends processes while sharing CPU time. | A browser and editor both remain responsive. |
| Memory management | Allocates RAM to programs and reclaims it when appropriate. | An application receives memory while it is running. |
| Device management | Coordinates hardware through drivers and system services. | Sends a print job to a printer. |
| File management | Organizes files and directories on storage and mediates access. | Saves a document into a folder. |
| User interface / shell | Lets a person control the computer using graphical or text-based tools. | Finder or a command-line shell. |
| Security and permissions | Checks identities and access rights for files and resources. | Prevents an unapproved account from editing a protected file. |

## 3. Commands / tools used
`sw_vers`, `uname`, `whoami`, `df`, `top`, `ps`, `pwd`, and `ls -l` are example tools. Platform options differ; use the version available on your operating system and list only commands you actually ran.

## 4. My understanding
The operating system manages shared resources so applications can run without each program controlling hardware directly. A process is a running program, storage capacity is different from memory in use, and permissions express what users may do with files. Absolute and relative paths name locations differently, which is why checking the current directory matters.

## 5. Difficulties faced
I was mixing up commands and making simple option errors.

## 6. How I resolved them
Keept a tab open with the command reference and used copy/paste to avoid typos.

## 7. Evidence / files
- This README contains example tables and explanations.
- A screenshots of the executed commands.

## 8. Commit details
- Commit message: `mission-03: Document operating system and file management`

