from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import smtplib
import os

# Load .env file for credentials
load_dotenv()

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

def send_email_notification():
    try:
        subject = "⚠️ WARNING: Gas & Vibration Detected"
        body = (
            "ALERT!\n\n"
            "Harmful gas and vibration have been detected by your sensors.\n"
            "Please check the environment immediately."
        )

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        print("[EMAIL] Text notification sent successfully!")
    except Exception as e:
        print(f"[EMAIL] Failed to send email: {e}")
