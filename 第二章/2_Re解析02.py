import re

str = '''
	<div class='jay'><span id='10010'>中国联通</span></div>
	<div class='jolin'><span id='10086'>中国移动</span></div>
	<div class='sular'><span id='10001'>中国电信</span></div>
'''

# re.S 让.能勾匹配换行符（默认.是不能匹配u换行符的）
# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取。
# (?P<span_Text>.*?) :（?P<aaa>xxxx） 将匹配到的xxx标识为aaa 方便后面.group('aaa')获取
obj = re.compile(r"<div class='(?P<class>.*?)'><span id='(?P<id>.*?)'>(?P<span_Text>.*?)</span></div>", re.S)

result = obj.finditer(str)

for it in result:
	print(it.group('class'))
	print(it.group('id'))
	print(it.group('span_Text'))
	print('========')
