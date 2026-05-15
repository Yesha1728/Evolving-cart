# Design Patterns Used

## Phase 1: Factory Method Pattern

### Where:
`src/item.py` — `ItemFactory` class

### Why:
Items were being created as plain unvalidated dictionaries inside ShoppingCart.
There was no central place for item creation and no way to enforce rules like
"price must be positive".

### What we gained:
- Centralized item creation in one place
- Added validation (negative price, zero quantity now raise errors)
- Easy to extend later (e.g. DigitalItem, PhysicalItem) without changing ShoppingCart
- ShoppingCart no longer needs to know HOW to create items

### Before:
```python
self.items.append({"name": name, "price": price, "quantity": quantity})
```

### After:
```python
item = ItemFactory.create(name, price, quantity)
self.items.append(item)
```

## Phase 2: Decorator Pattern

### Where:
`src/discount.py` — `CouponDecorator` class

### Why:
Discount logic was buried in if-else chains inside calculate_total().
Every new coupon or discount type required modifying the core method directly.

### What we gained:
- Each discount type is its own class
- Discounts can be stacked/layered on top of each other
- Adding a new discount never touches existing code (OCP!)
- Easy to test each discount in isolation

### Before:
```python
if self.coupon == "SAVE10":
    total = total - 10
elif self.coupon == "HALF":
    total = total * 0.50
```

### After:
```python
self.discount = CouponDecorator(self.discount, code)
total = self.discount.apply(raw_total)
```

---

## Phase 2: Facade Pattern

### Where:
`src/cart_facade.py` — `CartFacade` class

### Why:
Outside code had to know about ShoppingCart, ItemFactory, and discount
classes separately. Too much complexity exposed to the user.

### What we gained:
- One simple class to interact with the entire cart system
- Internal complexity is completely hidden
- Easy to change internals without affecting outside code

### Before:
```python
cart = ShoppingCart("vip")
cart.add_item("Laptop", 999.99, 1)
discount = VIPDiscount()
total = discount.apply(cart.calculate_total())
```

### After:
```python
facade = CartFacade("vip")
facade.add_item("Laptop", 999.99, 1)
facade.print_receipt()
```