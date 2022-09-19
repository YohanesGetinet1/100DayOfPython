from twilio.rest import Client

TWILIO_SID = "AC135319f*********9757fc68d"
TWILIO_AUTH_TOKEN = "40dbb********d5703831f0bf362"
TWILIO_VIRTUAL_NUMBER = "+135****435"
TWILIO_VERIFIED_NUMBER = "***********"


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
