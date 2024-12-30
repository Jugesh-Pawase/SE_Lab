import smtplib
import random

print("Program to verify OTP")
mail = input("Enter mail: ")
rotp = random.randint(100000, 999999)

def authMail(mail,otp):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = "jayzore6@gmail.com"
    TO_EMAIL = mail
    PASSWORD = "jay@4131"

    MESSAGE = f"""Subject: OTP Authentication

    Please use the verification code below to sign in.
    {otp}

    If you didn't request this, you can ignore this email."""

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.quit()

authMail(mail,rotp)
otp = input("Enter OTP: ")
if otp == str(rotp):
    print("Your OTP is correct")
else:
    print("Your OTP is wrong")
