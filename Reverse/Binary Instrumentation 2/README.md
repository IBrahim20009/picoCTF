# Binary Instrumentation 2 — Write-Up

## Description

This challenge continues the theme of inspecting Windows binaries and extracting hidden data using reverse-engineering tools. Similar to the previous challenge, the solution involves analyzing an executable and uncovering embedded content.

## Solution

### 1. Unzip the Challenge File

The provided archive is password protected:

```bash
unzip bininst2.zip
```

After entering the password, the extracted file `bininst2.exe` appears.

### 2. Analyze the Binary Using Binwalk

Run binwalk to detect compressed or embedded sections:

```bash
binwalk -e bininst2.exe
```

Binwalk reports LZMA-compressed data at offset `0x6000` and extracts it into the directory:

```
_bininst2.exe.extracted
```

### 3. Inspect the Extracted Files

Navigate into the extracted folder:

```bash
cd _bininst2.exe.extracted
ls
```

You should see two files:

```
6000
6000.7z
```

The file `6000` contains the decompressed binary content.

### 4. Search for Useful Strings

Use `strings` to pull readable text from the binary blob:

```bash
strings 6000
```

Among the output, an important Base64 string appears:

```
cGljb0NURntmcjFkYV9mMHJfYjFuX2luNXRydW0zbnQ0dGlvbiFfYjIxYWVmMzl9
```

### 5. Decode the Base64 String

Decode it using:

```bash
echo "cGljb0NURntmcjFkYV9mMHJfYjFuX2luNXRydW0zbnQ0dGlvbiFfYjIxYWVmMzl9" | base64 -d
```

This outputs:

```
picoCTF{fr1da_f0r_b1n_in5trum3nt4tion!_b21aef39}
```

## Final Flag

```
picoCTF{fr1da_f0r_b1n_in5trum3nt4tion!_b21aef39}
```

## Notes

* The challenge embeds the Base64 string directly inside the extracted binary content.
* `strings` is often helpful for quickly spotting CTF flags or encoded payloads.
* This challenge parallels the previous one, reinforcing the workflow of extracting and decoding hidden data from binaries.
