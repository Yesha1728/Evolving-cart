# src/cart_facade.py

from cart import ShoppingCart
from discount import (
    NoDiscount, MemberDiscount, VIPDiscount,
    StudentDiscount, CouponDecorator
)


class CartFacade:
    """
    Facade: simplifies the cart system for outside users.
    They only need to interact with this one class.
    """

    def __init__(self, user_type: str):
        self.cart = ShoppingCart(user_type)
        self.user_type = user_type
        self.coupon_code = None

        # Pick discount based on user type
        if user_type == "member":
            self.discount = MemberDiscount()
        elif user_type == "vip":
            self.discount = VIPDiscount()
        elif user_type == "student":
            self.discount = StudentDiscount()
        else:
            self.discount = NoDiscount()

    def add_item(self, name, price, quantity):
        self.cart.add_item(name, price, quantity)

    def remove_item(self, name):
        self.cart.remove_item(name)

    def apply_coupon(self, code):
        self.coupon_code = code
        self.discount = CouponDecorator(self.discount, code)

    def get_total(self):
        raw_total = sum(item.subtotal() for item in self.cart.items)
        return round(self.discount.apply(raw_total), 2)

    def print_receipt(self):
        print("===== RECEIPT =====")
        for item in self.cart.items:
            print(f"{item.name} x{item.quantity} - ${item.subtotal():.2f}")
        print(f"User type: {self.user_type}")
        if self.coupon_code:
            print(f"Coupon: {self.coupon_code}")
        print(f"TOTAL: ${self.get_total()}")
        print("===================")


if __name__ == "__main__":
    # Outside code only talks to CartFacade — simple!
    facade = CartFacade("vip")
    facade.add_item("Laptop", 999.99, 1)
    facade.add_item("Mouse", 29.99, 2)
    facade.apply_coupon("SAVE10")
    facade.print_receipt()