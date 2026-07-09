class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        item = {
            "name": name,
            "price": price
        }

        self.items.append(item)


    def total_price(self):
        total = 0

        for item in self.items:
            total += item["price"]

        return total



cart = ShoppingCart()

cart.add_item("Laptop", 80000)
cart.add_item("Mouse", 1500)
cart.add_item("Keyboard", 3000)
cart.add_item("Monitor", 20000)
cart.add_item("Headphone", 5000)

print("Total Price:", cart.total_price())