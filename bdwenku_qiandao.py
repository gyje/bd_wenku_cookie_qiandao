import requests as rq
import schedule
import time
headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': '换成你的cookie',
'Host': 'wenku.baidu.com',
'Referer': 'https://wenku.baidu.com/task/browse/daily',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
url = "https://wenku.baidu.com/task/submit/signin"

def sigin():
	result = rq.get(url,headers = headers)
	print(result)

schedule.every().day.at("10:30").do(sigin)

while 1:
	schedule.run_pending()
	time.sleep(1)
