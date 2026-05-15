# AI Log - Phase 2

## Prompt I asked:
"Adapter pattern burada uygun mu, yoksa Facade mı? Farkını açıkla."

## AI Response Summary:
AI explained that Adapter pattern is used when you have two incompatible
interfaces and need to make them work together. Facade on the other hand
is used to simplify a complex system behind one clean interface. Since our
cart system has multiple classes that work together but are complex to use
from outside, Facade was the right choice here, not Adapter.

AI also suggested Decorator for the discount layering problem, explaining
that Decorator adds behavior on top of existing objects without changing
them, which is exactly what we needed for stacking discounts.

## What I implemented:
- CouponDecorator in discount.py wraps any DiscountStrategy and adds
  coupon logic on top without modifying the original discount classes
- CartFacade in cart_facade.py hides ShoppingCart, ItemFactory, and
  discount classes behind one simple interface

## What AI got wrong or I disagreed with:
AI initially suggested using Bridge pattern instead of Decorator for
the discount system. Bridge is meant for separating abstraction from
implementation across two dimensions. Our discount problem is simpler —
we just need to layer behaviors, which is exactly what Decorator does.
So I rejected the Bridge suggestion and used Decorator instead.