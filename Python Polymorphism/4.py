class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")
student1 = student("shiva", 20)
teacher1 = teacher("vivek", "Maths")
student1.display()
teacher1.display()