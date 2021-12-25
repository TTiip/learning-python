# 1.定位到2021 必看电影
# 2.从2021必看电影中提取到子页面的连接地址
# 3.请求子页面的连接地址，拿到我们想要的下载地址

import requests
import re

# requests 移除SSL认证，输出InsecureRequestWarning提示的取消方法(python)
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

domain = 'https://dytt89.com/'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

# verify = False 去掉安全验证（https）
resp = requests.get(domain, headers=headers, verify=False)

# 指定字符集（改变编码方式）
resp.encoding = 'gb2312'

obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2= re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3= re.compile(
	r'◎译　　名　(?P<movie>.*?)<br />.*?<td '
	r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">'
, re.S)

result1= obj1.finditer(resp.text)
children_href_list = []

# 此处只有一个 养成良好习惯 finditer 生成的是数组 直接循环调用
for item in result1:
	ul = item.group('ul')
	# 提取子页面链接
	result2 = obj2.finditer(ul)
	for it in result2:
		# strip 去掉字符 类似于 js 中的replace 替换成 空
		children_href = domain.strip('/') + it.group('href')
		children_href_list.append(children_href)

# 通过子页面 请求获得下载地址
for href in children_href_list:
	children_resp = requests.get(href, headers=headers, verify=False)
	children_resp.encoding = 'gb2312'
	result3 = obj3.finditer(children_resp.text)

	for i in result3:
		print(i.group('movie'))
		print(i.group('download'))
		print('=============')
	# break # 只是测试用 跳出本次循环

resp.close()
children_resp.close()
