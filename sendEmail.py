import smtplib
import ssl
from email.mime.text import MIMEText


def send_alert():
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    email_user = "diego.carrarini@ifs-italia.it"
    email_pwd = "Bird.1978\\\\"
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(email_user, email_pwd)
        # TODO: Send email here
        server.sendmail(email_user, "diego.carrarini@ifs-italia.it", "MessageUI")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

def send_email():
    port = 587
    sender = 'diego.carrarini@ifs-italia.it'
    receiver = 'diego.carrarini@ifs-italia.it'
    msg = MIMEText('Secured test mail')
    msg['Subject'] = 'Test mail'
    msg['From'] = 'diego.carrarini@ifs-italia.it'
    msg['To'] = 'diego.carrarini@ifs-italia.it'
    user = 'diego.carrarini@ifs-italia.it'
    password = 'Bird.1978\\\\'
    with smtplib.SMTP("smtp.office365.com", port) as server:
        server.starttls()  # Secure the connection
        server.login(user, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("mail successfully sent")
