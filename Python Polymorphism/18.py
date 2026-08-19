class Person:
    def role(self):
        print("I am a person")
class Student(Person):
    def role(self):
        print("I am a student")
class Teacher(Person):
    def role(self):
        print("I am a teacher")
class Doctor(Person):
    def role(self):
        print("I am a doctor")
s = Student()
t = Teacher()
d = Doctor()
s.role()
t.role()
d.role()