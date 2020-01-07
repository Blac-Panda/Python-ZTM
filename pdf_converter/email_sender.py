import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Tunmise Oyefeso'
email['to'] = 'crispusomonze@gmail.com'
email['subjeect'] = 'Stop sleeping on the bicycle'

email.set_content('I am a Python Boss')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomastery@gmail.com', 'helloztmmyoldfriend1')
    smtp.send_message(email)
    print('all sent')