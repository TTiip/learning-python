# 安装requests
# pip install requests

# https://mirrors.tuna.tsinghua.edu.cn/ 清华源 国内依赖资源下载网站

# https://mirrors.tuna.tsinghua.edu.cn/help/pypi/ pip 国内下载资源

import requests
query = input('输入一个你喜欢的明星：')
url = f'https://www.sogou.com/web?query={query}'
# 请求头 标识请求设备（绕过反爬）
headers_obj = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

# 地址栏里面的请求 一定是get请求
resp = requests.get(url, headers=headers_obj)

# print(resp) # <Response [200]>
print(resp.text) # 拿到页面源代码
