import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 이메일 서버 설정
smtp_server = "smtp.gmail.com" 
smtp_port = 587 
email_address = "munjjac@gmail.com" 
password = "pmut pkif uiaw twdg" 

# 이메일 수신자 설정
recipient_email = "munjjac@hanmail.net" 

# 이메일 내용 생성
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = recipient_email
msg['Subject'] = "라즈베리파이에서 보낸 이메일"
message = "라즈베리파이에서 보내는 테스트 메시지입니다." 
msg.attach(MIMEText(message, 'plain'))

# SMTP 서버에 연결하고 이메일 보내기
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls() 
server.login(email_address, password)  
server.send_message(msg) 
server.quit()
