from email.message import EmailMessage
import ssl # (secure sockets layer)
import smtplib # (simple mail transfer protocol)
  

email_sender='nesrine.ncibi23@gmail.com'
email_password='cerxqtafrfxpwnbc'

email_receiver='nesrine.ncibi@polytechnicien.tn'

subject=":3"

body=":3"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver

em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, em.as_string())

