# 1.先拿到网页源代码提取子页面地址
# 2.找到图片链接然后下载
import requests
from bs4 import BeautifulSoup
import time
import re
import os

url = "https://pic.netbian.com/4kfengjing"  # /tupian/29312.html
url_1 = "https://pic.netbian.com/"  # 这个用于拼接找到图片页面
req = requests.get(url)
req.encoding = "gbk"
# print(req.text)
# 把源码交给bs
tup = BeautifulSoup(req.text, "html.parser")
lianjie = tup.find("ul", class_="clearfix")  # 把范围缩小find是找一个class_是因为里面本来就有那个啥子保留字
list = lianjie.find_all("a")  # 通过find_all来提取ul里面的a
obj = re.compile(r'<img alt=".*?src="(?P<download>.*?)"', re.S)
for a in list:
	# print(a.get("href"))#这里是通过a.get（）找到href里面的链接
	wangye = url_1 + a.get("href").strip("/")  # 直接通过get就可以获取链接然后和之前的主链接进行拼接获得新的图片链接
	# 获取子页面的源代码
	req_1 = requests.get(wangye)
	req_1.encoding = "gbk"
	# time.sleep(100)调试的时候用不然请求过快就会封ip
	photo = BeautifulSoup(req_1.text, "html.parser")
	photo_1 = photo.find("div", class_="photo-pic")  # 找特殊值或者就是只有一个出现的
	# print(photo_1)#这里拿到了图片的那个位置然后我们可以用find_all缩小范围
	photo_2 = photo_1.find("img")  # 拿到img标签位置
	photo_3 = str(photo_2)
	xiazai = obj.findall(photo_3)
	for b in xiazai:
		download_1 = url_1 + b.strip("/")
		print(download_1)
		# 下载图片
		download_2 = requests.get(download_1)
		# download_2.content#这里是拿到图片的字节然后我们写入就可以了
		# print(download_2.content)
		file_name = download_1.split("/")[-1]  # 文件名字
		# print(file_name)
		os.chdir("F:\桌面\平时源码\爬虫\img")
		with open(file_name, 'wb') as f:
			f.write(download_2.content)
		print("下载完成：", file_name, os.getcwd())
	time.sleep(2)
