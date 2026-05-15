# src/item.py

class Item:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise ValueError(f"Price cannot be negative: {price}")
        if quantity <= 0:
            raise ValueError(f"Quantity must be positive: {quantity}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return round(self.price * self.quantity, 2)

    def __repr__(self):
        return f"Item({self.name}, ${self.price}, x{self.quantity})"


class ItemFactory:
    @staticmethod
    def create(name, price, quantity):
        # Central place for creating items
        # Easy to extend later (e.g. DigitalItem, PhysicalItem)
        return Item(name, price, quantity)