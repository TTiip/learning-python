# 那页面源代码
# 获取和解析数据

import requests
from lxml import etree

query = input('请输入需要查找的信息: ')
url= f'https://beijing.zbj.com/search/f/?kw={query}&type=new'

resp = requests.get(url)

# HTML 将源码进行一个加载
# 注意XML和HTML不能混用
# 解析内容
html = etree.HTML(resp.text)

divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div/div')

for div in divs:
  price = div.xpath('.//div/a[2]/div[2]/div[1]/span[1]/text()')
  title = div.xpath('.//div/a[2]/div[2]/div[2]/p/text()')
  print(price)
  print(title)
  print('=========')

