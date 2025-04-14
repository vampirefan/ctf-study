# Notes for CTF study

## 学习笔记 (Notes)
- S1.AnHengNotes1-4: 第一次培训笔记
- S1.NCCNotes1-10: 第二次培训笔记
- writeups-buuctf: buuctf 做题笔记
- writeups-ctfhub: ctfhub 做题笔记

## 工具 (Tools)

### 环境
- [git](https://git-scm.com/downloads/win)
- [python](https://www.python.org/downloads/)
- [java8](https://www.java.com/zh-CN/download/?locale=zh_)
- [java21](https://www.oracle.com/java/technologies/downloads/)
- [go](https://golang.google.cn/dl/)
- [nodejs](https://github.com/nvm-sh/nvm)
- [docker](https://www.docker.com/)
- [wsl](https://learn.microsoft.com/zh-cn/windows/wsl/install)：Windows 上安装 Linux 虚拟机
- [clash-verge](https://clashcn.com/clash-verge-rev-releases)

### 加解密工具
- [CyberChef](https://github.com/gchq/CyberChef/releases)
- [jsons](http://www.jsons.cn/rabbitencrypt/)

### 抓包
- [yakit](https://github.com/yaklang/yakit)：安装后点击左上角铃铛来安装其证书
- [yakit-chrome-extension](https://github.com/yaklang/yaklang-chrome-extension): 浏览器代理切换插件
- [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega): 浏览器代理切换插件
- [burpsuite](https://portswigger.net/burp/releases/professional-community-2025-1-3)：将 `BurpLoaderKeygen.jar` 放在安装的根目录下，使用批处理脚本`start.bat`(内容为 `.\jre\bin\java.exe -jar BurpLoaderKeygen.jar`)进行启动。访问本机 8080 端口下载并安装 ca 证书。
- [burpLoaderKeygen](https://github.com/WankkoRee/BurpLoaderKeygenCnF): 破解 burpsuite
- [wireshark](https://www.wireshark.org/download.html)

### Sql 注入
- [sqlmap](https://github.com/sqlmapproject/sqlmap)

### 漏扫
- [xray](https://github.com/chaitin/xray): 一款功能强大的安全评估工具
- [fscan](https://github.com/shadow1ng/fscan)
- [WeblogicTool](https://github.com/KimJun1010/WeblogicTool): 需要使用 jre1.8 打开
- [WeblogicExploit-GUI](https://github.com/sp4zcmd/WeblogicExploit-GUI)
- [dirsearch](https://github.com/maurosoria/dirsearch)：扫描网站目录
- [feroxbuster](https://github.com/epi052/feroxbuster)：扫描网站目录
- [ffuf](https://github.com/ffuf/ffuf)：扫描网站目录
- [gobuster](https://github.com/OJ/gobuster/releases/tag/v3.6.0)：扫描网站目录
- [common.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt): 常见目录文件名
- [GitHack](https://github.com/lijiejie/GitHack)：扫描和下载 Git 泄露的日志文件
- [dvcs-ripper](https://github.com/kost/dvcs-ripper)：扫描和下载 SVN/Git/Hg 泄露日志文件

### webshell 管理器
利用文件上传漏洞
- [蚁剑antSword](https://github.com/AntSwordProject/antSword)
- [冰蝎Behinder](https://github.com/rebeyond/Behinder)
- [哥斯拉Godzilla](https://github.com/BeichenDream/Godzilla)

### 攻击及其他
- [frp](https://github.com/fatedier/frp)：frp 是一个专注于内网穿透的高性能的反向代理应用
- [httrack](https://www.httrack.com/page/2/en/index.html)：网站克隆下载工具

### 防御
- [蜜罐hfish](https://hfish.net/#/)
- [MySQL_Fake_Server](https://github.com/fnmsd/MySQL_Fake_Server)：假数据库

