import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_name = "Rauojia Djowd"
sender_email = "testingkkhm@gmail.com"
receiver_email = "chenray2003@gmail.com"
# google app password
password = "lfex lxfd mobt ajzq"

# Create message container
msg = MIMEMultipart()
msg['From'] = f"{sender_name} <{sender_email}>"
msg['To'] = receiver_email
msg['Subject'] = "App Registration verification code"

# Generate random code
random_code = random.randint(10000, 99999)

# Email body with HTML formatting for font size
body = f"<div style='font-size: 14px;'>Your code is: <strong>{random_code}</strong></div>"
msg.attach(MIMEText(body, 'html'))

# Create SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.send_message(msg)
server.quit()

# --------------------------------------------------------
input_code = input("the code is: \n")
while int(input_code) != random_code:
    print("wrong code, try it again")
    input_code = input("the code is: \n")

print("verified successful")
user_name = input("lets make a username: \n")
password_1 = input("make a password: \n")
while(len(password_1) < 5):
    password_1 = input("password minimum length is 6, try a another one\n")

password_2 = input("verify your password \n")
while password_1 != password_2:
    password_2 = input("wrong password: do it again\n")


print("registered successfully")
