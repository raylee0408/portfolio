import smtplib, ssl

host =  "smtp.gmail.com"
port = 465

username = "nzexcel007@gmail.com"
password = "xlqa sycg qmuu ccxp"

receiver = "nzexcel007@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: HI!
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message )

