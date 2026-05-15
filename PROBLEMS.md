# Problems in Initial Cart Code

## Problem 1: God Class
The `ShoppingCart` class does everything — manages items, calculates discounts,
applies coupons, AND prints receipts. One class should not have this many responsibilities.
This violates the Single Responsibility Principle (SRP).

## Problem 2: Hard-coded Discount Logic
All discount rules (member, vip, student) are buried inside `calculate_total()`.
Adding a new user type means editing this method directly, which can break existing logic.

## Problem 3: Hard-coded Coupon Logic
Coupon handling is also crammed inside `calculate_total()`. Every new coupon
requires modifying the core method, making the code fragile and hard to maintain.

## Problem 4: No Extensibility
There is no way to add a new discount type or coupon without touching and
potentially breaking the existing `calculate_total()` method. This violates
the Open/Closed Principle (OCP).

## Problem 5: Mixed Responsibilities in calculate_total()
One method is doing three jobs at once: summing items, applying user discounts,
and applying coupons. This makes it hard to test, debug, or change any one part.

## Problem 6: No Separation Between Data and Behavior
Items are stored as plain dictionaries instead of objects. This means there is
no validation, no structure, and behavior related to items is scattered around.

## AI Comparison
### What I found:
Problems 1 through 6 above.

### What AI found:
(We will fill this in after asking Claude/ChatGPT to review the code)

### Differences:
(To be filled in after AI comparison)

## AI Comparison

### What I found:
Problems 1-6 (God Class, hard-coded discounts, hard-coded coupons,
no extensibility, mixed responsibilities in calculate_total, no item objects)

### What AI found:
AI found the same core problems plus two additional ones:
- No Observer/notification system when cart changes
- calculate_total() doing 3 separate jobs should be broken into separate methods

### Differences:
AI spotted the missing Observer pattern opportunity which I hadn't thought of.
AI also suggested a Factory pattern specifically for Item creation with validation,
which was more specific than my general "no separation between data and behavior" point.
Overall our findings were very similar on the main problems.