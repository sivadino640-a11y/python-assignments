class Employee:
    def __init__(self, salary):
        self.salary = salary
    def __gt__(self, e):
        return self.salary > e.salary
e1 = Employee(50000)
e2 = Employee(30000)
print(e1 > e2)