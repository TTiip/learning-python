from lxml import etree

# etree.HTMLParser() 必须加上 否则报错 可以简单的理解为 按照HTML解析
tree = etree.parse('./a.html', etree.HTMLParser())

# result = tree.xpath('/html')

# reslut: ['百度', '谷歌', '搜狗']
# result = tree.xpath('/html/body/ul/li/a/text()')

# reslut: ['百度'] 取出第一个 注意 1 就代表 第一个 不是第二个
# [] 表示索引
# result = tree.xpath('/html/body/ul/li[1]/a/text()')

# result = ['feiji', 'dapao', 'huoche']
# @ 表示获取 标签的属性
# result = tree.xpath('/html/body/ol/li/a/@href')


# reslut = ['大炮']
# 表示当 标签a 的属性为dapao的 时候获取其文本
# result = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')


# ol_li_list = tree.xpath('/html/body/ol/li')
# for item in ol_li_list:
#   # 从每个item中提取文字信息
#   text = item.xpath('./a/text()') # 在item中继续查找，相对查找
#   href = item.xpath('./a/@href') # 获取属性 @属性
#   print(text)
#   print(href)

# ['http://www.baidu.com', 'http://www.google.com', 'http://www.sogou.com']
# print(tree.xpath('/html/body/ul/li/a/@href'))

