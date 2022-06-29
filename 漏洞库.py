import requests
from bs4 import BeautifulSoup
import re
import time
import csv

k = int(input("第几页结束"))

for n in range(1, k + 1):
	
	# n = int(input("第几页"))
	url = f"http://www.cnnvd.org.cn/web/cnnvdpatch/querylist.tag?pageno={n}"  # 访问这个网址拿取源码
	url_1 = "http://www.cnnvd.org.cn/"
	head = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
	}
	data = requests.get(url, headers=head)
	# print(data.text)
	bs = BeautifulSoup(data.text, "html.parser")
	# print(bs)
	positioning = bs.find("div", class_="list_list").find_all("a")  # 找到特殊位置进行筛选 不能_class 只可以class_
	obj = re.compile(r'meta name="title" content="(?P<name>.*?)"', re.S)  # 使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配
	# print(positioning)
	obj_2 = re.compile(r'</a><p><span>(?P<time>.*?).*?</span>(?P<time_1>.*?)</p>', re.S)  # 匹配时间的正则
	f = open("bugku.csv", "a+", encoding="utf-8")
	csv_writer = csv.writer(f)
	csv_writer.writerow(["漏洞名字", "修复措施", "发布时间"])
	for a in positioning:
		# print(a.get("href"))  # BeautifulSoup可以通过get直接拿到href里面的链接
		wangye = url_1 + a.get("href").strip("/")  # 拼接新链接
		req = requests.get(wangye)  # 通过get访问新链接
		# print(req.text)
		names = obj.findall(req.text)
		times = obj_2.finditer(req.text)  # 在req里面匹配时间整成元组
		for b in times:
			nams = names[-1]  # 漏洞名字
			uul = wangye  # 修复网页
			timetime = b.group("time") + b.group("time_1")  # 时间
			print(nams, uul, timetime)
			csv_writer.writerow([nams, uul, timetime])
		
		# time.sleep(2)
	
	f.close()
	time.sleep(15)
	print("休息15秒")
