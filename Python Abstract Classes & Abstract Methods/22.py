from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


car = Car("Toyota", "Camry")
bike = Bike("Honda", "Shine")

print(car.brand, car.model)
car.start()
car.stop()

print(bike.brand, bike.model)
bike.start()
bike.stop()