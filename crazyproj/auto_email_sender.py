import schedule
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def dend_email():
    sender_email = input("your_email@gmail.com: ")
    receivers_email = input("receivers_email@gmail.com: ")
    subject = "Scheduled Email"
    body = "Hello, this is an email sent from  REDTAIL cybersec company!"
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = input("enter username_email@gmail.com: ")
    smtp_password = input("enter your_email_password: ")
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receivers_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    server.sendmail(sender_email, receivers_email, message.as_string())
    
    server.quit()
    print("Email sent successfully!")
    
    schedule.every().day.at("09:00").do(sender_email)
    
    while True:
        schedule.run_pending()
        time.sleep(1)