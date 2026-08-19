numbers = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
even_count = sum(1 for n in numbers.values() if n % 2 == 0)
odd_count = sum(1 for n in numbers.values() if n % 2 != 0)
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")