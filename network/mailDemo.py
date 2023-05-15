import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendMail(title,receiver,From,to,subject):
    # 第三方SMTP服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="1246118299@qq.com"    #用户名
    mail_pass="howqiqmtuegbhfii"   #口令

    sender = "1246118299@qq.com"
    receivers = []
    receivers.append(receiver)

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(title, 'plain', 'utf-8') # 邮件内容
    message['From'] = Header(From, 'utf-8')  # 发送者
    message['To'] = Header(to, 'utf-8')  # 接收者
    # subject = 'Python SMTP 邮件测试' # 邮件标题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


