# AI Log - Phase 1

## Prompt I asked:
"Here is my Python code. What design problems do you see in it?
Which design patterns could fix these problems?"

## AI Response Summary:
AI identified the Factory Method pattern as appropriate for item creation.
It pointed out that plain dictionaries have no validation and that a proper
Item class with a factory would centralize creation and add safety checks.

## What I implemented:
Created an Item class with price and quantity validation, and an ItemFactory
with a static create() method. Updated ShoppingCart to use ItemFactory instead
of raw dictionaries.

## Differences from AI suggestion:
AI suggested considering an Abstract Factory for future item types (DigitalItem,
PhysicalItem). I chose a simpler Factory Method instead because we only have one
item type right now. Abstract Factory would be over-engineering at this stage.