from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        print("I am a Student")

class Teacher(Person):
    def role(self):
        print("I am a Teacher")


student = Student()
teacher = Teacher()

student.role()
teacher.role()