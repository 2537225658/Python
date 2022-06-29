import requests
import re
import csv

url = "http://movie.douban.com/top250"
headers = {
	"user-agent": "Mozilla/5.0(Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# 测试一下
obj = re.compile(
	r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
	r'class="rating_num" property="v:average">(?P<number>.*?)</span>', re.S)
f=open("date.csv","w")
write=csv.writer(f)
page_content = resp.text
ret = obj.finditer(page_content)
for it in ret:
	print("名字：",it.group("name").strip())
	print("上映时间：",it.group("year").strip())
	print("评分：",it.group("number").strip())
	dic=it.groupdict()
	write.writerow(dic.values())
f.close()
