students = {
    "ashik": 85,
    "vivek": 92,
    "siva": 78,
    "suresh": 96,
    "mahesh": 88
}
topper = max(students, key=students.get)
lowest_scorer = min(students, key=students.get)
print(f"Topper: {topper} with {students[topper]} marks.")
print(f"Lowest Scorer: {lowest_scorer} with {students[lowest_scorer]} marks.")