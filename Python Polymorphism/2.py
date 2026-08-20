class Car:
    def start(self):
        return "Car starting"
class Bike:
    def start(self):
        return "Bike starting"
class Bus:
    def start(self):
        return "Bus starting"
car = Car()
bike = Bike()
bus = Bus()
print(car.start())
print(bike.start())
print(bus.start())