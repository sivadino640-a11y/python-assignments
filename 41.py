std = {
    "ashik": 85,
    "vivek": 92,
    "siva": 78,
    "suresh": 96,
    "mahesh": 88
}

for student, mark in std.items():
    if mark > 75:
        print(f"{student}: {mark}")