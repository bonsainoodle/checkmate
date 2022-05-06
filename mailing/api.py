from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

from mailing.template import template


def connect(gmailUser, gmailPassword) -> smtplib.SMTP_SSL:
    """
    Creates the connection to the SMTP server
    """
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmailUser, gmailPassword)
        return server
    except:
        raise Exception("Could not connect to the SMTP server...")


def send_code(gmailUser, gmailPassword, to, guildName, memberName) -> int:
    """
    Sends the auth code to the user
    """
    code = f"{guildName[:3].upper()}{random.randint(1000, 9999)}"

    subject = f"Authentication code for {guildName}"

    html = template(guildName, memberName, code)

    body = MIMEText(html, "html")

    msg = MIMEMultipart("alternative")
    msg.attach(body)

    msg["Subject"] = subject
    msg["From"] = gmailUser
    msg["To"] = to

    try:
        server = connect(gmailUser, gmailPassword)

        server.sendmail(gmailUser, to, msg.as_string())
        server.close()

        return code
    except:
        raise Exception("Could not send the email...")
