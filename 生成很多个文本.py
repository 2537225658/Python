import os
import random
import string
i=1
os.chdir("F:\桌面\平时源码")
while i<100:
	filename = ''.join(random.sample(string.ascii_letters + string.digits, 8))
	newfile=filename+'.txt'
	f=open(newfile,'w+')
	for a in range(1,11):
		neirong=  ''.join(random.sample(string.ascii_letters + string.digits,10))
		f.write(neirong)
	i+=1
print(os.getcwd())

