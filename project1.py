from email.message import EmailMessage 
import ssl
import smtplib
from password import password
# Added environment variable support for email password

email_sender="katlalasyasridurga@gmail.com"
email_password=password

email_receiver="fosoli4546@marineso.com"

subject="This is a test email from python"
body="""
This is a test email sent from python using smtplib and email.message modules.
This email is sent for testing purposes only.
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
