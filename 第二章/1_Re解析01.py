import re

# findall：匹配字符串中所有的正则的内容
# 建议 正则前面加一个 r
findall_lstt = re.findall(r'\d+', '我和我的祖国：10086,他和对他的祖国：10010')

print(findall_lstt)
print('==========')

# finditer：匹配字符串中所有的内容（返回的是迭代器 里面的每一项都是match对象）,从迭代器中的拿到内容需要.group()
finditer_it= re.finditer(r'\d+', '我和我的祖国：10086,他和对他的祖国：10010')

for i in finditer_it:
	# 打印出每一项
	print(i.group())
print('==========')

# search：从其中的拿到内容需要.group() 注意： 找到一个节点就会返回
search_item= re.search(r'\d+', '我和我的祖国：10086,他和对他的祖国：10010')

print(search_item.group())
print('==========')

# match：从头开始匹配 可以理解为 以这个开头
match_item= re.match(r'\d+', '我和我的祖国：10086,他和对他的祖国：10010')

print(match_item.group())
print('==========')

# 预加载正则表达式
# 为了提高 性能
# obj = re.compile(r'\d+')