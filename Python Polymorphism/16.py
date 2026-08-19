class Notification:
    def send(self):
        print("Sending notification")
class Email(Notification):
    def send(self):
        print("Sending Email")
class SMS(Notification):
    def send(self):
        print("Sending SMS")
class WhatsApp(Notification):
    def send(self):
        print("Sending WhatsApp")
e = Email()
s = SMS()
w = WhatsApp()
e.send()
s.send()
w.send()