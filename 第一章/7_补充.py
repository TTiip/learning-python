import requests
# 第一种
# url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20'

# 第二种
# 重新封装参数
url = 'https://movie.douban.com/j/chart/top_list'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

params = {
	'type': 17,
	'interval_id': '100:90',
	'action': '',
	'start': 0,
	'limit': 20,
}

# header不能使用 headers 这种简写方式 必须使用 headers=headers 这种方式传递
resp = requests.get(url, params, headers = headers)

print(resp.json())

# 避免 keep-alive 导致 请求次数过多的问题
resp.close() # 关掉resp
