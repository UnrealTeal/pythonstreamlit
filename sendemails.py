import streamlit as st # <- display your python project/app
from email.message import EmailMessage # <- Email configuration: Sender, receiver, content/body, attachment
import ssl # <- keeps email secure, no one reads but the reciever
import smtplib # <- Simple mail transfer protocall: responsible to send mail from sender to reciever

sender = "githubtee@gmail.com"
password = "cczaelfrzzyywngz"

receiver = st.text_input("Type email to send to: ")
subject = st.text_input("Insert email subject here: ")
body = st.text_area("Insert email content here: ",height=200)

if st.button("Send Email"):
    # EMAIL CONFIG
    email = EmailMessage()# creates new email message
    email["From"] = sender
    email["To"] = receiver
    email["subject"] = subject
    email.set_content(body) # content of the email that was sent

    #email SSL
    emailssl = ssl.create_default_context() # creates secure connection: noone can recieve the mail

    #Send email via smtp
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=emailssl) as smtp: # hostname, port and ssl
        # This helps connect to gmail server
        smtp.login(sender, password) # this login to sender email address with sender password
        smtp.sendmail(sender,receiver,email.as_string())
        st.success("Email sent!, Thank you")