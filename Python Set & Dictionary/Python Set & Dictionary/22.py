numbers = {10, 25, 5, 40, 15}
smallest = None
for n in numbers:
    if smallest is None or n < smallest:
        smallest = n
print(smallest)