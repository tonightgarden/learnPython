from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = input('15995117160@163.com')
password = input('0929tgqp')
# 输入收件人地址:
to_addr = input('tg991@foxmail.com')
# 输入SMTP服务器地址:
smtp_server = input('smtp.163.com')

import smtplib
#server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()