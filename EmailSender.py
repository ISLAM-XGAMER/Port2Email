import smtplib
from email.message import EmailMessage
import sys

def userinfo(sender_email2 , receiver_email2 , password2):
        
        
    global sender_email , receiver_email , password
        
    sender_email =  sender_email2
    receiver_email = receiver_email2
    password = password2




def send(portnum , ip , status):

        
           
    message = EmailMessage()
    if status == "o":
        message.set_content(f'The port {portnum} is open for the ip {ip}')
    else:
        message.set_content(f'The port {portnum} is closed for the ip {ip}')
        
    message['Subject'] = 'Port Scanner'
    message['From'] = sender_email
    message['To'] = receiver_email


    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.send_message(message)
        server.quit()
        print("All ports are scanned and the results are sent to your email")
    except smtplib.SMTPAuthenticationError : # wrong username or password
        print("wrong Email or password , please try again with the correct ones".title())
        sys.exit()
        