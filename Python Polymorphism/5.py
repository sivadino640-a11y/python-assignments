class emailnotification:
    def send_email(self):
        return "Sending email notification"
class smsnotification:
    def send_sms(self):
        return "Sending SMS notification"
email = emailnotification()
sms = smsnotification()
print(email.send_email())
print(sms.send_sms())