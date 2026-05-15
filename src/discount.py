# src/discount.py

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class MemberDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.90  # 10% off


class VIPDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.80  # 20% off


class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.85  # 15% off


class CouponDecorator(DiscountStrategy):
    def __init__(self, wrapped: DiscountStrategy, coupon_code: str):
        self.wrapped = wrapped
        self.coupon_code = coupon_code

    def apply(self, total: float) -> float:
        total = self.wrapped.apply(total)
        if self.coupon_code == "SAVE10":
            return total - 10
        elif self.coupon_code == "HALF":
            return total * 0.50
        return total