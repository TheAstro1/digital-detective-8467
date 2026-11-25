# Mission 4 — How programs run

## 1. Task / objective
Run a short Python program and compare how compilers and interpreters translate or execute programs.

## 2. Work completed
[`hello.py`](hello.py) prints `Hello from Python`. From the repository root, run it with:

```bash
python3 mission-04-programs/hello.py
```

Expected output:

```text
Hello from Python
```

### Compiler and interpreter comparison
| Point | Compiler | Interpreter |
|---|---|---|
| When execution happens | Translates source into a separate executable or other target before execution. | executes source or an intermediate representation at runtime. |
| Typical output | A native executable or object code, depending on the toolchain. | Runtime results; some implementations also create bytecode or other intermediate forms. |
| Example | C program compiled with a C compiler. | Python program run by a Python implementation. |
| One advantage | A compiled native program can run without translating the source on every launch. | Interactive execution and rapid experimentation can be convenient. |

A compiler commonly translates a program into a target form before that program runs, while an interpreter commonly carries out instructions at runtime. The distinction is not absolute: real language implementations can combine techniques. For example, CPython compiles Python source to bytecode and its virtual machine executes that bytecode.

## 3. Commands / tools used
| Command or tool | Purpose |
|---|---|
| `python3 mission-04-programs/hello.py` | Run the example using Python 3. |
| Text editor | Create and inspect `hello.py` and this comparison. |

## 4. My understanding
A source file contains instructions, and a language implementation turns those instructions into actions the computer can perform. “Compiled” and “interpreted” describe common execution approaches, not a strict division where every language uses only one method. Running a tiny program confirms that the interpreter is available and that the file executes.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [`hello.py`](hello.py) — runnable one-line Python program.
- This README — run command and comparison.

## 8. Commit details
- Commit message: `mission-04: Compare compilers and interpreters`

