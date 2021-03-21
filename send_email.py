import smtplib
from email.message import EmailMessage

print("Connecting to the server..")
with smtplib.SMTP(host='smtp.gmail.com' , port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    #get the sender email and password
    print("----- Enter your login information -----")
    while True:
        sender_email = input("Enter your email: ")
        sender_password = input("Enter your password: ")#use a third-app party password
        print("Logging...")
        try:
            if smtp.login(sender_email,sender_password):
                print("Login Done!")
                email = EmailMessage()
                email['from'] = input("From: ")
                email['to']= input("To: ")
                email['subject'] = input("Subject: ")
                email_content = input("Content of the email: ")
                email.set_content(email_content)
                smtp.send_message(email)
                print("Email Sent !")
                break
        except smtplib.SMTPAuthenticationError as err:
            print("--> Username or password incorrect ! try again\n",err)




