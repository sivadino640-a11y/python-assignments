from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary: 80000")


class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary: 60000")


manager = Manager("Rahul", 101)
developer = Developer("Priya", 102)

print(manager.name, manager.employee_id)
manager.calculate_salary()

print(developer.name, developer.employee_id)
developer.calculate_salary()