# AI Log - Phase 3

## Pair Programming Session (30+ minutes)

### What we discussed:
I used Claude as my AI pair programming partner for Phase 3.
We discussed how to implement the Observer pattern in the cart system
and how Strategy pattern was already partially present in Phase 2.

### Prompts I asked:
1. "How does the Observer pattern work? Show me a simple example."
2. "How can I add Observer pattern to my CartFacade class?"
3. "Is my Observer implementation following the Open/Closed Principle?"

### AI Response Summary:
AI explained that Observer pattern has two parts:
- Subject (the cart) that maintains a list of observers and notifies them
- Observers that react to events without the cart knowing their details

AI confirmed my implementation follows OCP correctly — adding a new
observer type (like EmailObserver) requires zero changes to CartFacade.

### What I implemented:
- CartObserver abstract base class in observer.py
- LoggerObserver that logs all cart events
- StockObserver that reserves/releases stock on item changes
- CartFacade updated to maintain observer list and notify on every event

### Where AI helped:
AI suggested using a dictionary for event data instead of positional
arguments, which made the observer update() method much more flexible
and readable.

### Where AI was wrong or I disagreed:
AI initially suggested making CartFacade inherit from an Observable
base class. I disagreed because CartFacade already inherits complexity
from being a Facade. Composition (having a list of observers) is
cleaner than inheritance here. I kept my original approach.

### How long without AI?
Without AI this phase would have taken at least 3-4 extra hours.
AI sped up un