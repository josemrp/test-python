# Docs:
# https://docs.python.org/3/library/smtplib.html

from smtplib import SMTP

host = "smtp.gmail.com"
port = 587
username = "" # Your email
password = "" # Your password
form_email = username
to_emails = [username]

smtp = SMTP(host, port)
smtp.ehlo()
smtp.starttls()

try:
  smtp.login(username, password)
  smtp.sendmail(form_email, to_emails, "Hello jose, I am using python")
  print("Email send")
except:
  print("An error has occurred")

smtp.quit()




