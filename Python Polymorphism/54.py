class Notification:
    def send(self):
        pass
class Email(Notification):
    def send(self):
        print("Email notification")
class SMS(Notification):
    def send(self):
        print("SMS notification")
class WhatsApp(Notification):
    def send(self):
        print("WhatsApp notification")
Email().send()
SMS().send()
WhatsApp().send()