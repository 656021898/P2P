import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.ReadConfig import ReadConfig
import configparser
from common.GetPath import GetPath
import os

subject = "HTTP test result"
#构造邮件对象MIMEMultipart
msg = MIMEMultipart("mixed")
msg["Subjet"] = subject
msg["From"] = "13355781026@163.com <13355781026@163.com>"
msg["To"] = "13355781026@163.com"


#构造附件
sendfile = open(os.path.join(GetPath.get_path(), ReadConfig("Excel","ExcelReadName").readConfig()),"rb").read()
text_att = MIMEText(sendfile,_charset="utf-8")
text_att["Content_Type"] = "application/octet-stream"
msg.attach(text_att)

#构造正文
html = """
<html>
  <head>HTTP test result heade</head>
  <body>
    <p>这是测试报告<br>
       查收后请回复<br>
    </p>
  </body>
</html>
"""
text_html = MIMEText(html,"html","utf-8")
text_html["Content-Disposition"] = "attachment; filename='texthtml.html'"
msg.attach(text_html)



smtp = smtplib.SMTP()
smtp.connect(host="smtp.163.com")
smtp.login(user="13355781026@163.com",password="qq13355781026")
smtp.sendmail(from_addr="13355781026@163.com",to_addrs="656021898@qq.com",msg=msg.as_string())
smtp.quit()