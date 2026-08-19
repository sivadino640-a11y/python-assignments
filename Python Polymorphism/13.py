class Employee:
    def calculate_salary(self):
        print("Employee salary is calculated")
class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary: ₹80,000")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: ₹60,000")
employees = [Manager(), Developer()]
for employee in employees:
    employee.calculate_salary()