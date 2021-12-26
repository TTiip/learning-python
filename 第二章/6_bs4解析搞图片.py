# 1.拿到主页面源代码，然后提取子页面的链接地址，href
# 2.通过href拿到子页面的内容，从子页面中找到图片下载地址 img --> src
# 3.下载图片

import requests
from bs4 import BeautifulSoup
import time
import os

domain = 'https://www.umei.cc/'
url = domain + 'bizhitupian/weimeibizhi/'
# 如果没有 文件夹 则创建文件夹
if not os.path.exists('./img'):
	# 目录不存在创建，makedirs可以创建多级目录
	os.mkdir('./img')

resp = requests.get(url)
resp.encoding = 'utf-8'

soup = BeautifulSoup(resp.text, 'html.parser')

# 获取图片列表
type_list = soup.find('div', attrs={ 'class': 'TypeList' })

href_list = type_list.find_all('a')
for item in href_list:
	# 通过get就可以拿到属性的值
	href = item.get('href')
	# 拿到子页面的源代码
	children_resp = requests.get(domain.strip('/') + href)
	children_resp.encoding = 'utf-8'
	children_soup = BeautifulSoup(children_resp.text, 'html.parser')
	# 分析得到图片的src
	children_title = children_soup.find('div', attrs={ 'class': 'ArticleTitle' }).find('strong').text
	children_src = children_soup.find('div', attrs={ 'class': 'ImageBody' }).find('img').get('src')

	# file_path_dir = os.path.dirname(f'./img/{children_title}.jpg')
	# 下载地址
	get_img = requests.get(children_src)
	# get_img.content --> 这里获取的图片流（）字节

	# 图片内容 写入文件
	with open(f'./img/{children_title}.jpg', mode='wb') as f:
		f.write(get_img.content)
		f.close()
		get_img.close()
	print(f'{children_title} -- download success!')
	# 休息一秒钟 防止 脚本被杀
	time.sleep(3)

resp.close()
children_resp.close()
print('all success!')

