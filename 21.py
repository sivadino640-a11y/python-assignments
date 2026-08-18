numbers = {10, 25, 5, 40, 15}
largest = None
for n in numbers:
    if largest is None or n > largest:
        largest = n
print(largest)