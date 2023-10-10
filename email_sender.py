import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'svetlana.oloinic@gmail.com'
email['to'] = 'svetkaolo17@gmail.com'
email['subject'] = 'You won 1 000 000 dollars!'


email.set_content('I am a Python Master')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('svetlana.oloinic@gmail.com', 'zarm xaus zqsj dolo')
  smtp.send_message(email)
  print('all good boss!')
