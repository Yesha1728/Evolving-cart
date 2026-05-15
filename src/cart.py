# class ShoppingCart:
#     def __init__(self, user_type):
#         self.items = []
#         self.user_type = user_type
#         self.coupon = None
#
#     def add_item(self, name, price, quantity):
#         self.items.append({"name": name, "price": price, "quantity": quantity})
#
#     def remove_item(self, name):
#         self.items = [i for i in self.items if i["name"] != name]
#
#     def apply_coupon(self, code):
#         self.coupon = code
#
#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item["price"] * item["quantity"]
#
#         if self.user_type == "member":
#             total = total * 0.90
#         elif self.user_type == "vip":
#             total = total * 0.80
#         elif self.user_type == "student":
#             total = total * 0.85
#         else:
#             total = total
#
#         if self.coupon == "SAVE10":
#             total = total - 10
#         elif self.coupon == "HALF":
#             total = total * 0.50
#         elif self.coupon == "FREESHIP":
#             total = total
#         else:
#             pass
#
#         return round(total, 2)
#
#     def print_receipt(self):
#         print("===== RECEIPT =====")
#         for item in self.items:
#             print(f"{item['name']} x{item['quantity']} - ${item['price'] * item['quantity']:.2f}")
#         print(f"User type: {self.user_type}")
#         if self.coupon:
#             print(f"Coupon: {self.coupon}")
#         print(f"TOTAL: ${self.calculate_total()}")
#         print("===================")
#
# if __name__ == "__main__":
#     cart = ShoppingCart("vip")
#     cart.add_item("Laptop", 999.99, 1)
#     cart.add_item("Mouse", 29.99, 2)
#     cart.apply_coupon("SAVE10")
#     cart.print_receipt()

# src/cart.py

from item import ItemFactory

class ShoppingCart:
    def __init__(self, user_type):
        self.items = []
        self.user_type = user_type
        self.coupon = None

    def add_item(self, name, price, quantity):
        item = ItemFactory.create(name, price, quantity)
        self.items.append(item)

    def remove_item(self, name):
        self.items = [i for i in self.items if i.name != name]

    def apply_coupon(self, code):
        self.coupon = code

    def calculate_total(self):
        total = sum(item.subtotal() for item in self.items)

        if self.user_type == "member":
            total = total * 0.90
        elif self.user_type == "vip":
            total = total * 0.80
        elif self.user_type == "student":
            total = total * 0.85

        if self.coupon == "SAVE10":
            total = total - 10
        elif self.coupon == "HALF":
            total = total * 0.50

        return round(total, 2)

    def print_receipt(self):
        print("===== RECEIPT =====")
        for item in self.items:
            print(f"{item.name} x{item.quantity} - ${item.subtotal():.2f}")
        print(f"User type: {self.user_type}")
        if self.coupon:
            print(f"Coupon: {self.coupon}")
        print(f"TOTAL: ${self.calculate_total()}")
        print("===================")


if __name__ == "__main__":
    cart = ShoppingCart("vip")
    cart.add_item("Laptop", 999.99, 1)
    cart.add_item("Mouse", 29.99, 2)
    cart.apply_coupon("SAVE10")
    cart.print_receipt()