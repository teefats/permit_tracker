import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail():
    #Email Account
    email_sender_account = "gloti3483@gmail.com"
    email_sender_username = "Tunde Fatusin"
    email_sender_password = "SlobodanMilosevic"
    email_smtp_server = "smtp.gmail.com"
    email_smtp_port = 587
    #Email Content
    email_recepients = ["teefats@gmail.com","tee_fats@yahoo.com"]
    email_subject = "Hello"
    email_body = "How do you do"
    
    server = smtplib.SMTP(email_smtp_server,email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)
    #For loop, sending emails to all email recipients
    for recipient in email_recepients:
        print(f"Sending email to {recipient}")
        message = MIMEMultipart('alternative')
        message['From'] = email_sender_account
        message['To'] = recipient
        message['Subject'] = email_subject
        message.attach(MIMEText(email_body, 'html'))
        text = message.as_string()
        server.sendmail(email_sender_account,recipient,text)
    #All emails sent, log out.
    server.quit()