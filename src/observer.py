# src/observer.py

from abc import ABC, abstractmethod


class CartObserver(ABC):
    @abstractmethod
    def update(self, event: str, data: dict):
        pass


class LoggerObserver(CartObserver):
    def update(self, event: str, data: dict):
        print(f"[LOG] Event: {event} | Data: {data}")


class StockObserver(CartObserver):
    def update(self, event: str, data: dict):
        if event == "item_added":
            print(f"[STOCK] Reserving stock for: {data['name']} x{data['quantity']}")
        elif event == "item_removed":
            print(f"[STOCK] Releasing stock for: {data['name']}")