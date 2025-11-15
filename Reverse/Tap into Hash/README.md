# 🔐 Blockchain Cipher Reverse Engineering — Write-Up

## 📌 Overview

This challenge provides an **encrypted blockchain**, a **key**, and a custom Python script that performs decryption and token extraction. Our task is to:

1. **Decrypt** the ciphertext using the provided key.
2. **Understand the block structure** of the decrypted data.
3. **Extract a hidden token** inserted inside the blockchain string.
4. **Recover and display the original blockchain hashes.**

We analyze the logic implemented in the provided Python scripts and reconstruct how the final output is derived.

---

## 📁 Files Provided

### **1. solve.py** (or decryption helper) fileciteturn3file0

This script:

* XOR-decrypts the given ciphertext
* Uses a SHA-256 hash of the key as the XOR pad
* Removes PKCS-style padding
* Extracts a token that was embedded inside the blockchain
* Reconstructs the original blockchain hash list

### **2. block_chain.py** (challenge generator)

*(If provided, describes how the encrypted output was originally created.)*

### **3. enc_flag**

Encrypted blockchain + token (ciphertext).

---

# 🧠 Understanding the Decryption Algorithm

### ✔ XOR Decryption

The encryption is simple XOR using a SHA-256-derived key:

```python
key_hash = hashlib.sha256(key).digest()
plaintext = xor(cipher_block, key_hash)
```

Each 16-byte block of ciphertext is XORed with the same 32-byte hash.

### ✔ Block Size and Padding

* Ciphertext is processed in 16-byte blocks.
* Padding is removed using:

```python
padding_length = plaintext[-1]
plaintext = plaintext[:-padding_length]
```

---

# ⛓️ Blockchain Format

The decrypted text contains:

* **5 SHA-256 block hashes**, each 64 characters
* Separated by **4 hyphens**

Total expected length:

```
5 × 64 chars + 4 dashes = 324 characters
```

But the ciphertext **has a hidden token inserted in the middle**. The solver must:

1. Split the decrypted string into *first half* of blockchain
2. Identify the embedded token
3. Append the remaining blockchain hash section

---

# 🔍 Extracting the Embedded Token

The extraction logic:

```python
midpoint = blockchain_length // 2
first_part = decrypted_text[:midpoint]
remaining = decrypted_text[midpoint:]
second_part = remaining[-(blockchain_length - midpoint):]
token = remaining[:-(blockchain_length - midpoint)]
```

Meaning:

* Everything “extra” in the decrypted text is the **token**.
* The original blockchain is reconstructed by reconnecting:

```
first_part + second_part
```

---

# ▶️ Running the Solver

Run the script:

```bash
python3 solve.py
```

You will see:

* Full decrypted text
* Extracted token
* Restored blockchain
* Individual block hashes

Example output:

```
Blockchain string:
<hash1>-<hash2>-<hash3>-<hash4>-<hash5>

Embedded token:
picoCTF{...}
```

---

# 🎉 Final Results

Running the solver will show:

* **The original blockchain** (5 SHA-256 hashes)
* **The hidden embedded token** (your flag)

Your exact flag appears under:

```
Embedded token:
```

inside the program output.

---

# 🧠 Key Takeaways

* XOR ciphers are weak when keys repeat.
* SHA-256 hashed keys add complexity but do not fix XOR weaknesses.
* Blockchain data was not actually blockchain — just concatenated SHA-256 hashes.
* Hidden data inserted inside a structured format can be extracted by using expected length.
