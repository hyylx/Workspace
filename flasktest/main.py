from email.mime.text import MIMEText

msg = MIMEText('hello!','plain', 'utf-8')
# 构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype('plain'表示纯文本，utf-8保证多语言兼容性)

from_addr = input('from: ')
password = input('Password: ')
to_addr = input('To: ')

smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server,25)#默认端口25
server.set_debuglevel(1)# 打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr,[to_addr],msg.as_string())#收件人是一个list因为可以一次发给多个人| 邮件正文要是str
server.quit()

#if __name__ == "__main__":
#    app.run(debug=True , host='0.0.0.0')

