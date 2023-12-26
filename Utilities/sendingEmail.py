import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("pmriganka707@gmail.com", "27NHXAK2")
server.sendmail("pmriganka707@gmail.com", "mrigankap707@gmail.com", "Email Utility")
server.quit()