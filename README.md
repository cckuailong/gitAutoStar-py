## GitStar 最新版（python3 开发）

### 参数配置

配置settings.py文件
```
IP         = "47.95.194.180" # GitStar IP
GITSTAR_NAME		= "" # GitStar用户名
GITSTAR_PASSWORD	= "" # GitStar密码
GIT_NAME		= "" # GitHub用户名
GIT_PASSWORD	= "" # GitHub密码
```
### 使用说明
```
cd venv/bin/
python gitStar.py   # 需要root权限
```

特别注意，这里依赖chrome浏览器，需要安装chrome浏览器，下载自己chrome版本对应的chromedriver，将chromedriver放到环境变量目录中，我这里用的linux，我直接扔到/usr/bin/中了，windows，mac的大兄弟如果不会，自行百度吧。。。

附上chromedriver下载地址： [传送门](http://chromedriver.storage.googleapis.com/index.html)
