products = {
    "apple": 5,
    "banana": 15,
    "orange": 8,
    "grape": 12,
    "mango": 3
}
for product, quantity in products.items():
    if quantity < 10:
        print(f"{product}: {quantity}")