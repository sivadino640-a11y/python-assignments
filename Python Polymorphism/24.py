class EmailService:
    def send(self):
        print("Sending message by Email")
class SMSService:
    def send(self):
        print("Sending message by SMS")
def send_message(service):
    service.send()
email = EmailService()
sms = SMSService()
send_message(email)
send_message(sms)