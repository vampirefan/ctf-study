# [第一章 web入门]常见的搜集
试了好些类似 dirsearch 的工具，都不好用，最后还是看的答案
- [dirsearch](https://github.com/maurosoria/dirsearch)：扫描网站目录
- [feroxbuster](https://github.com/epi052/feroxbuster)：扫描网站目录
- [ffuf](https://github.com/ffuf/ffuf)：扫描网站目录
- [gobuster](https://github.com/OJ/gobuster/releases/tag/v3.6.0)：扫描网站目录
- [common.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt): 常见目录文件名
反正最后就是要查出来几个文件
```
robots.txt -> flag1:n1book{info_1
index.php~ -> flag2:s_v3ry_im
.index.php.swp -> flag3:p0rtant_hack}

n1book{info_1s_v3ry_imp0rtant_hack}
```
