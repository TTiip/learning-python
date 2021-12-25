# 1.定位到2021 必看电影
# 2.从2021必看电影中提取到子页面的连接地址
# 3.请求子页面的连接地址，拿到我们想要的下载地址

import requests
import re

# requests 移除SSL认证，输出InsecureRequestWarning提示的取消方法(python)
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://dytt89.com/'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

# verify = False 去掉安全验证（https）
resp = requests.get(url, headers=headers, verify=False)

# 指定字符集（改变编码方式）
resp.encoding = 'gb2312'

obj = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
result= obj.finditer(resp.text)

# 此处只有一个 养成良好习惯 finditer 生成的是数组 直接循环调用
for item in result:
	ul = item.group('ul')

# print(resp.text)