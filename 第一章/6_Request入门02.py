import requests

url = 'https://fanyi.baidu.com/sug'

s = input('输入你需要翻译的词：')

data_obj = {
	'kw': s
}

# 发送的参数放到对象中 通过data参数进行传递
resp = requests.post(url, data=data_obj)

print(resp.json()) # 服务器返回的内同出街处理成json