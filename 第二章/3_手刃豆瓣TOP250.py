# 拿到页面源代码 request
# 通过re来提取想要的有效信息 re

import requests
import re
import csv

url = 'https://movie.douban.com/top250'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

resp = requests.get(url, headers=headers)
page_content= resp.text

# 需要正则匹配的规则
obj = re.compile(
	r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<rate>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>'
, re.S)

# 正则匹配的内容
result = obj.finditer(page_content)

# 在相对路径下创建一个data.csv文件
# 记得指定编码类型
f = open('./data.csv', mode='w', encoding='utf-8')
# 调用csv模块 类似于生成实例对象。
csvwriter = csv.writer(f)

for item in result:
	# print('name', item.group('name'))
	# print('year', item.group('year').strip()) # strip() 去掉空格并换行
	# print('rate', item.group('rate').strip()) # strip() 去掉空格并换行
	# print('num', item.group('num').strip()) # strip() 去掉空格并换行
	# print('==================')

	# 创建一个字典
	dic = item.groupdict()
	dic['year'] = dic['year'].strip()
	dic['rate'] = dic['rate'].strip()
	dic['num'] = dic['num'].strip()
	# 在字典中 插入每一行的数据
	# 注意是 values 是方法
	csvwriter.writerow(dic.values())

f.close()

print('success!')
