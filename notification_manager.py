from twilio.rest import Client
import smtplib

TWILIO_SID = "ACa0bfb37ce89b2182189b6482e7614b71"
TWILIO_AUTH_TOKEN = "d2e6d59511dcefb9c67cd479acf802be"
TWILIO_VIRTUAL_NUMBER = "+18174354113"
TWILIO_VERIFIED_NUMBER = "+959966565693"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "aungchan391@gmail.com"
MY_PASSWORD = "123456channyein"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')

                )
