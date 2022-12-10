import smtplib
import ssl
from email.mime.text import MIMEText
import configparser as configparser



def send_email():
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    server = config['EMAIL']['smtp_server']
    port = config['EMAIL']['smtp_port']
    sender = config['EMAIL']['smtp_username']
    receiver = config['EMAIL']['smtp_to']
    msg = MIMEText('Secured test mail')
    msg['Subject'] = config['EMAIL']['smtp_subject']
    msg['From'] = config['EMAIL']['smtp_from']
    msg['To'] = config['EMAIL']['smtp_to']
    user = config['EMAIL']['smtp_username']
    password = config['EMAIL']['smtp_password']
    with smtplib.SMTP(server, port) as server:
        server.starttls()  # Secure the connection
        server.login(user, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("mail successfully sent")
        server.quit()
