# Mission 5 — Numbers and data

## 1. Task / objective
Convert values between decimal, binary, and hexadecimal by hand; verify them with Python; build a small converter; and explain text encoding.

## 2. Work completed
### Manual conversions
| Question | Working | Answer |
|---|---|---|
| Decimal 13 to binary | 13 = 8 + 4 + 1 = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ | `1101₂` |
| Decimal 25 to binary | 25 = 16 + 8 + 1 = 1×2⁴ + 1×2³ + 0×2² + 0×2¹ + 1×2⁰ | `11001₂` |
| Binary `1010` to decimal | 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 2 | `10₁₀` |
| Binary `1101` to decimal | 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 1 | `13₁₀` |
| Hexadecimal `A` to decimal | `A` represents 10 in base 16. | `10₁₀` |
| Hexadecimal `1F` to decimal | 1×16¹ + 15×16⁰ = 16 + 15 | `31₁₀` |
| Binary `1111` to hexadecimal | `1111₂` = 15 decimal; digit F represents 15 in base 16. | `F₁₆` |

### Python verification
These expressions use Python's built-in conversions and match the manual results:

| Conversion | Python expression | Result |
|---|---|---|
| Decimal 13 → binary | `bin(13)` | `'0b1101'` |
| Decimal 25 → binary | `bin(25)` | `'0b11001'` |
| Binary `1010` → decimal | `int('1010', 2)` | `10` |
| Binary `1101` → decimal | `int('1101', 2)` | `13` |
| Decimal 13 → hexadecimal | `hex(13)` | `'0xd'` |
| Decimal 25 → hexadecimal | `hex(25)` | `'0x19'` |
| Hexadecimal `A` → decimal | `int('A', 16)` | `10` |
| Hexadecimal `1F` → decimal | `int('1F', 16)` | `31` |

`bin()` and `hex()` include base prefixes (`0b` and `0x`). The prefix identifies the representation; it is not part of the digits themselves.

### Number converter
Run from the repository root:

```bash
python3 mission-05-numbers-data/number_converter.py
```

Sample tests:

| Input | Binary output | Hexadecimal output |
|---:|---|---|
| `13` | `0b1101` | `0xd` |
| `25` | `0b11001` | `0x19` |
| `255` | `0b11111111` | `0xff` |

The program reads text with `input()`, parses a whole number using `int()`, then calls `bin()` and `hex()` to produce the two base-prefixed representations. If the input is not a valid integer, it displays a helpful error instead of a traceback.

### Text encoding
The ASCII decimal code for uppercase `A` is 65; lowercase `a` is 97. An encoding standard maps characters to numbers/bytes so software can store and interpret text consistently. A character such as `é` or `🙂` is not part of basic ASCII; UTF-8 can represent these and many other characters.

## 3. Commands / tools used
| Command or tool | Purpose |
|---|---|
| `python3` | Run the converter and Python conversion expressions. |
| `input()` / `int()` | Read the entry and convert decimal text to an integer. |
| `bin()` / `hex()` | Produce binary and hexadecimal strings. |
| `int(value, base)` | Parse strings written in binary or hexadecimal. |

## 4. My understanding
Each positional digit represents a power of its number base. In binary the place values are powers of two; hexadecimal uses powers of sixteen and digits A–F for values ten through fifteen. Python's conversion functions are useful checks, but writing out place values shows why the answer is correct. Text encodings provide a shared mapping from characters to stored data.

## 5. Difficulties faced
No major difficulties, other than needing to write down the values while dry runs.

## 6. How I resolved them
had a notebook with me.

## 7. Evidence / files
- [`number_converter.py`](number_converter.py) — interactive decimal-to-binary/hexadecimal converter.
- This README — worked conversions, Python checks, sample tests, and encoding notes.
- A screenshot of the converter running with a test values.

## 8. Commit details
- Commit message: `mission-05: Build number converter and practise data representation`

