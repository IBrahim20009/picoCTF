###Solve

# Linux Commands
apktool d filename.apk , the d option provides for you decompiling the .apk file , the b makes the oppsite


# Find the folders 
if you ask ChatGPT or Claude they will say that the flag often will be in this path "values/strings.xml"

# Cat the strings.xml file 
If we cat the strings.xml file you will see a Base32 text in the beginning of the content 

`OBUWG32DKRDHWMLUL53TI43OG5PWQNDSMRPXK3TSGR3DG3BRNY4V65DIGNPW2MDCGFWDGX3DGBSDG7I=`

if we use cyberchef or the base32 command in linx with echo we can get the flag 



`echo "OBUWG32DKRDHWMLUL53TI43OG5PWQNDSMRPXK3TSGR3DG3BRNY4V65DIGNPW2MDCGFWDGX3DGBSDG7I=" | base32 -d`

the flag will be : `picoCTF{1t_w4sn7_h4rd_unr4v3l1n9_th3_m0b1l3_c0d3}`


