from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary: 80000")

    def display_details(self):
        print("Manager: Manages the team")


class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary: 60000")

    def display_details(self):
        print("Developer: Writes and maintains code")


manager = Manager()
developer = Developer()

manager.calculate_salary()
manager.display_details()

developer.calculate_salary()
developer.display_details()