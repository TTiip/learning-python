# 爬虫：通过白那些程序来获取互联网上的资源
# 百度
# 需求：用程序模拟浏览器，来输入一个网址，冲网址中获取到资源或者内容

# python搞定以上需求：

from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)

# print(resp.read().decode('utf-8'))

# 此处 生成的文件会有乱码 记得在open函数中 加一个 encoding='utf-8' 参数即可解决!!!

with open('./mybaidu.html', mode='w', encoding='utf-8') as f:
	f.write(resp.read().decode('utf-8')) # 读取到网页的页面源代码
print('success！')