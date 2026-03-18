import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_cpu_temperature():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=", "").replace("'C\n", "")
    return float(temp)

def send_email(subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address = "munjjac@gmail.com" 
    password = "pmut pkif uiaw twdg" 
    recipient_email = "munjjac@hanmail.net"

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, password)
    server.send_message(msg)
    server.quit()

while True:
    cpu_temp = get_cpu_temperature()
    print(f"Current CPU Temperature: {cpu_temp}°C")
    subject = "라즈베리파이 CPU 온도 알림"
    message = f"현재 CPU 온도: {cpu_temp}°C"

    send_email(subject, message)
    time.sleep(600)  # 10분 동안 대기
