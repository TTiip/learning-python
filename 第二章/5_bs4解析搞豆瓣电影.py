# bs4解析比较简单，但是需要分析html标签去解析。
# 安装 pip install bs4

# 1.拿到页面源代码
# 2.使用bs4进行解析，拿到数据

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://movie.douban.com/top250'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}
f = open('./movie.csv', mode='w', encoding='utf-8')

cvs_writer = csv.writer(f)

resp = requests.get(url, headers=headers)

# 解析数据
# 1.把页面源代码用BeautifulSoup解析，生成bs对象

# html.parser 用来指定 html解析器
page_content= BeautifulSoup(resp.text, 'html.parser')

# 2.从bs对象中查找数据
# find （标签，属性=值）
# find_all （标签，属性=值）

# class 是关键字（保留字）!!!!

# class_ 用来匹配class
# ol = page_content.find('ol', class_='grid_view')

# attrs 来匹配属性
ol = page_content.find('ol', attrs={ 'class': 'grid_view' })

# 拿到所有的数据 从第二条数据开始切片（即从第二条数据开始）
li_item = ol.find_all('div', attrs={ 'class': 'item' })[1:]
for item in li_item:
	title = item.find('span', attrs={ 'class': 'title' }).text
	rating_num = item.find('span', attrs={ 'class': 'rating_num' }).text
	img_src = item.find('img', attrs={ 'class': '' }).get('src')
	cvs_writer.writerow([title, rating_num, img_src])

resp.close()
print('success!')