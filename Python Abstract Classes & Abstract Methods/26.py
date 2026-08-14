from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Manager(Employee):
    def work(self):
        print(self.name, "manages the team")


class Developer(Employee):
    def work(self):
        print(self.name, "develops software")


class Tester(Employee):
    def work(self):
        print(self.name, "tests software")


manager = Manager("Rahul", 80000)
developer = Developer("Priya", 60000)
tester = Tester("Amit", 50000)

print(manager.name, manager.salary)
manager.work()

print(developer.name, developer.salary)
developer.work()

print(tester.name, tester.salary)
tester.work()