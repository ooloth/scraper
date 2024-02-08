import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_notification(
    subject: str, body: str, to: str, gmail_user: str, gmail_password: str
):
    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(gmail_user, to, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
