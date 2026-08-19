class Vehicle:
    def start(self):
       print("vehcile starting")
class Car(Vehicle):
    def start(self):
        print("car starting")
class Bike(Vehicle):
    def start(self):
        print("bike starting")
class Bus(Vehicle):
    def start(self):
        print("bus starting")
vehicles = [Car(), Bike(), Bus()]
for vehicle in vehicles:
    vehicle.start()