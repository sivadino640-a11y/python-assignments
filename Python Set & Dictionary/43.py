employees = {
    "mahesh": 50000,
    "vivek": 60000,
    "siva": 55000,
    "suresh": 65000,
    "ashik": 58000
}

for employee, salary in employees.items():
    if salary > 50000:
        print(f"{employee}: ₹{salary}")