class Computer:
    def process(self):
        print("Computer is processing")
class Laptop(Computer):
    def process(self):
        print("Laptop is processing")
class Desktop(Computer):
    def process(self):
        print("Desktop is processing")
class Server(Computer):
    def process(self):
        print("Server is processing")
l = Laptop()
d = Desktop()
s = Server()
l.process()
d.process()
s.process()