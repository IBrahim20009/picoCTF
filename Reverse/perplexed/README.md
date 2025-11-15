# Bit-Mapping Reverse Engineering Challenge — Write-Up

## 📌 Overview

This challenge revolves around reversing a **custom bit-scrambling algorithm** used to validate an unknown password. The data we are given is an encoded byte array and knowledge of how the original verification function behaved.

Your goal: **reverse the bit-mapping logic and reconstruct the original password.**

The included file `solve.py` contains a full tracing tool that analyzes the algorithm and reconstructs the password.

---

## 📁 Files Used

* `solve.py` — tracing & reconstruction script

---

## 🧠 Understanding the Algorithm

The original check compares specific bits of the user input against bits in an encoded array. These internal variables control the mapping:

| Variable   | Meaning                    |
| ---------- | -------------------------- |
| `local_1c` | input byte index           |
| `local_20` | input bit position (1–7)   |
| `local_28` | encoded bit position (0–7) |
| `local_24` | encoded byte index         |

The comparison logic:

```
input_bit[local_1c][7 - local_20] == encoded_bit[local_24][7 - local_28]
```

### Key Observations

* **Bit 0 of each input byte is never used.**
* Each output byte therefore uses **only 7 meaningful bits**.
* The encoded byte array is effectively a continuous **7-bit packed bitstream**.

This explains why a simple 8-bit reconstruction fails.

---

## 🧪 Step 1 — Tracing the Mapping

`solve.py` traces how bits flow:

```
encoded[0][bit7] → input[0][bit6]
encoded[0][bit6] → input[0][bit5]
...
```

This reveals exactly how the encoded stream maps into the password.

---

## 🔁 Step 2 — First Reconstruction Attempt

The script tries direct reconstruction:

```python
result[local_1c] |= (1 << (7 - local_20))
```

This generates 27 bytes, but they are *not valid ASCII* — proving the algorithm packs only 7 bits per output byte.

---

## 🔓 Step 3 — Correct Repacking Method

The script then performs the proper reverse process:

1. Extract all **184 bits** from the encoded array.
2. Repack the bits into **7-bit bytes**.
3. Convert the resulting bytes into ASCII.

This produces a valid ASCII password.

---

## 🎉 Final Output

Running the script prints:

* The traced bit mapping
* The raw reconstructed bytes
* Their hex representation
* The final decoded password

To get the final password:

```bash
python3 solve.py
```

The password appears on the last line of the output.

---

## ▶️ How to Run

```bash
python3 solve.py
```

Expect output like:

```
Tracing first few iterations...
Reconstructed bytes...
Decoded: "your_final_password"
```

---

## 🧠 Key Takeaways

* The challenge uses an unusual **7-bit packing scheme**.
* Bit-level tracing is crucial in reversing obfuscated checks.
* When bit 0 is never written, the algorithm is likely using **7-bit ASCII packing**.
* Reconstructing the bitstream and repacking it solves the challenge.

---

## 📦 Want Improvements?

I can add:

* A diagram of the bit flow
* A simplified solver script
* A GitHub-style project structure
* Beginner-friendly explanations

Just tell me: **"Add more detail"** or **"Add diagrams"**.
