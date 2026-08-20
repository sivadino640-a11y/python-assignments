class emailnotification:
    def send_email(self):
        return "email notification"
class smsnotification:
    def send_sms(self):
        return "SMS notification"
email = emailnotification()
sms = smsnotification()
print(email.send_email())
print(sms.send_sms())