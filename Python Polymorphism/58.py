class Password:
    def login(self):
        print("Login with Password")
class OTP:
    def login(self):
        print("Login with OTP")
class Biometric:
    def login(self):
        print("Login with Fingerprint")
p = Password()
o = OTP()
b = Biometric()
p.login()
o.login()
b.login()