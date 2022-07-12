# 发送多种类型的邮件这是一个基于python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
os.getcwd()
msg_from = '2632565822@qq.com'  # 发送方邮箱账号
passwd = ''  # 就是上面的授权码

to = [
	]  # 接受方邮箱添加的话就用逗号隔开

# 设置邮件内容
# MIMEMultipart类可以放任何内容也可以放附件什么的都可以放
msg = MIMEMultipart()
conntent = "漏洞推送"
# 把内容加进去
msg.attach(MIMEText(conntent, 'plain', 'utf-8'))
my_file = os.path.isfile('./bugku.csv')
if my_file == True:
	os.renames(r"bugku.csv", "bugku.xlsx")  # 先把他转化为表格
else:
	pass
# 添加附件
add = MIMEText(open('bugku.xlsx', 'rb').read(), 'base64', 'utf-8')  # 打开附件
add["Content-Type"] = 'application/octet-stream'
add["Content-Disposition"] = 'attachment; filename="bugku.xlsx"'
msg.attach(add)
# 设置邮件主题
msg['Subject'] = "重庆简检小安科技有限公司"

# 发送方信息
msg['From'] = msg_from

# 开始发送

# 通过SSL方式发送，服务器地址和端口
s = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 登录邮箱
s.login(msg_from, passwd)
# 开始发送
s.sendmail(msg_from, to, msg.as_string())
print("邮件发送成功")
