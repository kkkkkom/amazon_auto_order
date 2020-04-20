
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
#with open(textfile) as fp:
#    # Create a text/plain message
#    msg = EmailMessage()
#    msg.set_content(fp.read())

def send_mail(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'instacart-notification@gmail.com'
    msg['To'] = <your email address>

    msg2 = EmailMessage()
    msg2.set_content(body)
    msg2['Subject'] = subject
    msg2['From'] = 'instacart-notification@gmail.com'
    msg2['To'] = <your 2nd email address>

    # Send the message via our own SMTP server.
    #s = smtplib.SMTP('localhost')
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(<your email address>, <your email password>)
    s.send_message(msg)
    s.send_message(msg2)
    s.close()
    print(f'Sent email to <your email address>: {subject}')
    print(f'Sent email to <your 2nd email address>: {subject}')
