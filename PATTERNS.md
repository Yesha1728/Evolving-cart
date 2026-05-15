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

## Phase 3: Observer Pattern

### Where:
`src/observer.py` — `CartObserver`, `LoggerObserver`, `StockObserver`
`src/cart_facade.py` — observer registration and notification

### Why:
Nothing happened when the cart changed. No logging, no stock updates,
no notifications. Adding these directly into CartFacade would bloat it
and violate Single Responsibility Principle.

### What we gained:
- Cart doesn't need to know WHO is listening or WHAT they do
- Adding a new observer (e.g. EmailObserver) requires ZERO changes to CartFacade
- This is a perfect example of Open/Closed Principle in action
- Each observer has one job and can be tested independently

### Open/Closed Principle demonstration:
To add email notifications, we just create a new class:
```python
class EmailObserver(CartObserver):
    def update(self, event: str, data: dict):
        print(f"[EMAIL] Sending notification for: {event}")
```
And register it — no existing code is touched!

---

## Phase 3: Strategy Pattern

### Where:
`src/discount.py` — `DiscountStrategy`, `MemberDiscount`, `VIPDiscount`,
`StudentDiscount`, `NoDiscount`

### Why:
Discount algorithms were hard-coded inside calculate_total() with if-else
chains. Switching discount types at runtime was impossible.

### What we gained:
- Each discount algorithm is its own swappable class
- Discount can be changed at runtime by swapping the strategy object
- Adding new discount types never touches existing code
- Combined with Decorator for coupon stacking