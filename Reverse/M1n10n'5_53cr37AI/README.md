# Mobile Reverse Engineering Challenge — Write-Up

## 🔍 Overview

In this challenge, we analyze an Android application (.apk) to extract a hidden flag. The `.apk` file contains resources that can be decompiled and inspected, revealing encoded data that we can decode to obtain the final flag.

---

## 🛠️ Tools & Commands

### **1. Decompile the APK using Apktool**

Use Apktool to extract and decompile the APK file:

```bash
apktool d filename.apk
```

* `d` → decompile
* `b` → recompile (not needed here)

This command generates a folder containing the full directory structure of the APK.

---

## 📁 Finding the Relevant Files

Commonly, CTF flags in Android challenges are stored in:

```
res/values/strings.xml
```

In this challenge, the flag-related data is indeed inside that file.

---

## 🧵 Inspecting `strings.xml`

To view the file:

```bash
cat res/values/strings.xml
```

Near the beginning of the file, you will notice this Base32-encoded string:

```
OBUWG32DKRDHWMLUL53TI43OG5PWQNDSMRPXK3TSGR3DG3BRNY4V65DIGNPW2MDCGFWDGX3DGBSDG7I=
```

---

## 🔓 Decode the Base32 String

You can decode Base32 using either **CyberChef** or the Linux CLI:

```bash
echo "OBUWG32DKRDHWMLUL53TI43OG5PWQNDSMRPXK3TSGR3DG3BRNY4V65DIGNPW2MDCGFWDGX3DGBSDG7I=" | base32 -d
```

---

## 🏁 Final Flag

```
picoCTF{1t_w4sn7_h4rd_unr4v3l1n9_th3_m0b1l3_c0d3}
```

---

If you'd like, I can:

* Add images/screenshots
* Expand explanations of APK structure
* Add a section on using JADX or MobSF
* Format this as a GitHub project template
