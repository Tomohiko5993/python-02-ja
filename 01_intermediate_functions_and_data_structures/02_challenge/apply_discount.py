def apply_discount(products, minimum_price, discount_rate):
    # 商品をフィルタリングし、割引を適用してタプルのリストを作成
    discounted_products = [
        (product["name"], (lambda price: price * (1 - discount_rate / 100))(product["price"]))
        for product in products if product["price"] >= minimum_price
    ]
    return discounted_products

# Example usage:
products1 = [
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]

products2 = [
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]

print(apply_discount(products1, 50, 10))  # Output: [('Laptop', 1080.0), ('Jacket', 90.0)]
print(apply_discount(products2, 100, 15)) # Output: [('Smartphone', 680.0), ('Sneakers', 102.0)]