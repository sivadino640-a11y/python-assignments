student = {
    "shiva": 80,
    "vivek": 90,
    "mahesh": 75
}

name = input("Enter student name: ")

if name in student:
    print("Student exists")
    print("Marks:", student[name])
else:
    print("Student does not exist")