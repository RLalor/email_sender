import smtplib
import getpass

# todo fix the problem of getpass not working in terminal or displaying asterixs
# todo you can also add date, time, attachments etc to the program

# ehlo needs to be the very next line of code to greet the server or u get errors
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)  # alt try port 465
smtp_object.ehlo()
print(smtp_object.starttls())
# email = input('email: ')
# uip = input('pw: ')
email = getpass.getpass("To login enter your email: ")
uip = getpass.getpass("Enter your password: ")
smtp_object.login(email, uip)
from_address = email
to_address = input("Enter recipients email: ")
subject = input("Enter the subject line: ")
message = input("Enter the message body: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address, to_address, msg)
print("Email sent.")
smtp_object.quit()
