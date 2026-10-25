# ByteBites backend models
#
# Customer  - a campus user: name + purchase history (list of past Orders)
# FoodItem  - one item we sell: name, price, category, popularity rating
# Menu      - the full list of FoodItems; filters by category and sorts
# Order     - one transaction: the FoodItems a customer picked + the total cost
#
# Classes relate by composition: Menu and Order hold FoodItems, Customer holds Orders.
# No class inherits from another.

from __future__ import annotations


class FoodItem:
    """One item ByteBites sells."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self) -> str:
        return (
            f"FoodItem({self.name!r}, ${self.price:.2f}, "
            f"{self.category!r}, rating={self.popularity_rating})"
        )


class Menu:
    """The full collection of FoodItems."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []


class Order:
    """A single transaction: the items a customer picked."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []


class Customer:
    """A ByteBites user with a name and a history of past orders."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.purchase_history: list[Order] = []

    def __repr__(self) -> str:
        return f"Customer({self.name!r}, orders={len(self.purchase_history)})"
