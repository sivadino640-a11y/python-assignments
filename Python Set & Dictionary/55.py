products = {
    "tv": 60000,
    "phone": 30000,
    "mouse": 1500,
    "tv": 45000,
    "keyboard": 2500
}

expensive_products = set()

for product, price in products.items():
    if price > 5000:
        expensive_products.add(product)

print("Products above ₹5,000:", expensive_products)