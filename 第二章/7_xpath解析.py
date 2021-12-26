# Xpath 是在XML文档中搜索内容的一门语言
# html是xml的一个子集

# 安装 lxml 模块
# pip install lxml


# xpath解析

from lxml import etree

xml = '''
<book>
	<id>1</id>
	<name>野花遍地香</name>
	<price>1.23</price>
	<nick>臭豆腐</nick>
	<author>
		<nick id='10086'>中国移动</nick>
		<nick id='10010'>中国联通</nick>
		<nick id='10001'>中国电信</nick>
		<div>
			<nick>惹了1</nick>
		</div>
  	<div>
			<nick>惹了2</nick>
			<span>
				<nick>惹了3</nick>
			</span>
		</div>
	</author>
	<partner>
		<nick id='ppc'>胖胖陈</nick>
		<nick id='ppbc'>胖胖不陈</nick>
  </partner>
</book>
'''

tree = etree.XML(xml)

# result = tree.xpath('/book')
# result = tree.xpath('/book/name')

# text() 是获取文本 result:['野花遍地香']
# result = tree.xpath('/book/name/text()')


# // 找后代 全部符合的 result:['中国移动', '中国联通', '中国电信', '惹了1', '惹了2', '惹了3']
# result = tree.xpath('/book/author//nick/text()')

# * 任意节点 通配符 result：['惹了1', '惹了2']
# result = tree.xpath('/book/author/*/nick/text()')

# result：['臭豆腐', '中国移动', '中国联通', '中国电信', '惹了1', '惹了2', '惹了3', '胖胖陈', '胖胖不陈']
result = tree.xpath('/book//nick/text()')
print(result)