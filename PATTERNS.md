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