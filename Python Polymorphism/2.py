class Car:
    def start(self):
        return "Car is starting"
class Bike:
    def start(self):
        return "Bike is starting"
class Bus:
    def start(self):
        return "Bus is starting"
car = Car()
bike = Bike()
bus = Bus()
print(car.start())
print(bike.start())
print(bus.start())