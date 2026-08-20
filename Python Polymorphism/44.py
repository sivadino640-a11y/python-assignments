class Student:
    def __init__(self, marks):
        self.marks = marks
    def __gt__(self, s):
        return self.marks > s.marks
s1 = Student(80)
s2 = Student(70)
print(s1 > s2)