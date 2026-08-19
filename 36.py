products = {
    "Laptop": 50000,
    "Pen": 20,
    "Mobile": 15000,
    "Bag": 800,
    "Headphones": 2000
}

for product in products:
    if products[product] > 1000:
        print(product, products[product])