# Challenge Write-Up

## Description

There are many ways to approach this challenge, but the method used here involves extracting embedded data using `binwalk`.

## Solution

### Steps

1. Run binwalk to extract the embedded files:

   ```bash
   binwalk -e bininst1.exe
   ```
2. Move into the extracted directory:

   ```bash
   cd _bininst1.exe.extracted
   ```
3. View the file named `6000`:

   ```bash
   cat 6000
   ```

Inside the file, you will find a Base64-encoded string:

```
cGljb0NURnt3NGtlX20zX3VwX3cxdGhfZnIxZGFfZjI3YWNjMzh9
```

4. Decode the Base64 string:

   ```bash
   echo "cGljb0NURnt3NGtlX20zX3VwX3cxdGhfZnIxZGFfZjI3YWNjMzh9" | base64 -d
   ```

### Flag

```
picoCTF{w4ke_m3_up_w1th_fr1da_f27acc38}
```
