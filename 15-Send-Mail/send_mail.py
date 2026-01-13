import smtplib
import ssl
from email.message import EmailMessage

# this config is from https://ethereal.email/, show more information in the end page
smtp_server = "smtp.ethereal.email"
smtp_port = 587
sender_email = "sallie.maggio84@ethereal.email"
password = "5aCMxZ6tnuNFgceKU6"

class EmailSender:
    def __init__(self, sender_mail, password, smtp_server, smtp_port):
        self.sender_mail = sender_mail
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send(self, receiver_email, subject, body):
        em = EmailMessage()
        em['From'] = self.sender_mail
        em['to'] = receiver_email
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
            smtp.starttls(context=context)
            smtp.login(self.sender_mail, self.password)
            smtp.send_message(em)

        print("Email send successfully")

sender = EmailSender(sender_email, password, smtp_server, smtp_port)
sender.send(sender_email, "Hello from Python!", "This is a Test!")


#Match the port to the method:
#465 → SMTP_SSL
#587 → SMTP + starttls()
#Typical SMTP configurations
#Gmail
#Server: smtp.gmail.com
#Port: 465 (SSL) OR 587 (STARTTLS)
#Password: App Password required
#Outlook / Office365
#Server: smtp.office365.com
#Port: 587 (STARTTLS)