import smtplib
from email.mime.text import MIMEText
from email.header import Header


def email_notification(receiver, subject, content):
    '''email notification'''
    mail_host = "smtp.xx.com"   # smtp.qq.com
    mail_user = "xx@xx.com"     # 用户名
    mail_pass = "xxxxxx"        # 授权码

    sender = 'isongxw@foxmail.com'

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "isongxw@foxmail.com"
    message['To'] = "isongxw@foxmail.com"

    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("Email notification succeeded")
    except smtplib.SMTPException:
        print("Email notification failed")


if __name__ == '__main__':
    email_notification("isongxw@foxmail.com", "text", "dsds")
