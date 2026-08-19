students = ["shiva", "mahesh", "vivek", "suresh", "karthik", "Revanth"]

count = {}

for name in students:
    if name in count:
        count[name] += 1
    else:
        count[name] = 1

print("Student list:", students)
print("Occurrences:", count)