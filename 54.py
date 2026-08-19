marks1 = {
    "vivek": 80,
    "Siva": 75,
    "karthik": 90
}
marks2 = {
    "vivek": 85,
    "Siva": 88,
    "mahesh": 95
}
common_students = set(marks1.keys()) & set(marks2.keys())
print("Students in both dictionaries:", common_students)