students = {
    "ashik": 85,
    "vivek": 92,
    "siva": 78,
    "suresh": 96,
    "mahesh": 88
}

highest_student = None
highest_mark = float('-inf')

for student, mark in students.items():
    if mark > highest_mark:
        highest_mark = mark
        highest_student = student

print("The student with the highest marks is {highest_student} with {highest_mark} marks.")