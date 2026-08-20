class Vehicle:
    def start(self):
        pass
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Start")
    def stop(self):
        print("Car Stop")
class Bike(Vehicle):
    def start(self):
        print("Bike Start")
    def stop(self):
        print("Bike Stop")
class Bus(Vehicle):
    def start(self):
        print("Bus Start")
    def stop(self):
        print("Bus Stop")
Car().start()
Car().stop()
Bike().start()
Bike().stop()
Bus().start()
Bus().stop()