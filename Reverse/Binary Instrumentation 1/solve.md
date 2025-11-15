<h1>Description</h1>

<p>There are alot of ways we can solve this challenge, but I use `binwalk -e <file>`</p>

<h1>Solve</h1>

<h3>Command</h3>

<p>`binwalk -e bininst1.exe` , then `cd _bininst1.exe.extracted ` and `cat 6000`</p>
<p>There is a base64 text `cGljb0NURnt3NGtlX20zX3VwX3cxdGhfZnIxZGFfZjI3YWNjMzh9`, decode it `echo "cGljb0NURnt3NGtlX20zX3VwX3cxdGhfZnIxZGFfZjI3YWNjMzh9" | base64 -d `</p>
<p>The flag is :`picoCTF{w4ke_m3_up_w1th_fr1da_f27acc38}`</p>
