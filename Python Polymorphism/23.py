class Car:
    def start(self):
        print("Car starts")
class Bike:
    def start(self):
        print("Bike starts")
def start_vehicle(vehicle):
    vehicle.start()
car = Car()
bike = Bike()
start_vehicle(car)
start_vehicle(bike)