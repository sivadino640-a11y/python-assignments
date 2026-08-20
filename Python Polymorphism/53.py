class Employee:
    def calculate_salary(self):
        pass
class FullTime(Employee):
    def calculate_salary(self):
        return 30000
class PartTime(Employee):
    def calculate_salary(self):
        return 15000
class Intern(Employee):
    def calculate_salary(self):
        return 10000
print(FullTime().calculate_salary())
print(PartTime().calculate_salary())
print(Intern().calculate_salary())