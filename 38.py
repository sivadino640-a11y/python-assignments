print("Create a dictionary of employee names and salaries. Calculate the average salary.")
employees = {
    "mahesh": 50000,
    "vivek": 60000,
    "siva": 55000,
    "suresh": 65000,
    "ashik": 58000
}

total_salary = sum(employees.values())
average_salary = total_salary / len(employees)

print(f"The average salary is {average_salary}.")