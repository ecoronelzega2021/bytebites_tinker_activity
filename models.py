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

    def add_item(self, item: FoodItem) -> None:
        """Add a FoodItem to the menu."""
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the items in the given category. Case and extra spaces are ignored."""
        wanted = category.strip().lower()
        return [item for item in self.items if item.category.strip().lower() == wanted]

    def sort_by_popularity(self) -> list[FoodItem]:
        """Return a new list of items, most popular first. self.items is not changed."""
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Order:
    """A single transaction: the items a customer picked."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a FoodItem to this order."""
        self.items.append(item)

    def calculate_total(self) -> float:
        """Return the total cost of the order, rounded to cents. An empty order is 0.0."""
        return round(sum(item.price for item in self.items), 2)

    def __repr__(self) -> str:
        return f"Order(items={len(self.items)}, total=${self.calculate_total():.2f})"


class Customer:
    """A ByteBites user with a name and a history of past orders."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.purchase_history: list[Order] = []

    def add_order(self, order: Order) -> None:
        """Record a completed order in this customer's history."""
        self.purchase_history.append(order)

    def is_verified(self) -> bool:
        """A customer counts as a real user once they have at least one past order."""
        return len(self.purchase_history) > 0

    def __repr__(self) -> str:
        return f"Customer({self.name!r}, orders={len(self.purchase_history)})"


if __name__ == "__main__":
    # Quick manual scenario: build a menu, filter, sort, place an order.
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 10.00, "Mains", 4.6))
    menu.add_item(FoodItem("Large Soda", 5.00, "Drinks", 3.8))
    menu.add_item(FoodItem("Cold Brew", 4.25, "Drinks", 4.9))
    menu.add_item(FoodItem("Chocolate Chip Cookie", 2.50, "Desserts", 4.4))
    menu.add_item(FoodItem("Tomato Soup", 6.00, "Soups", 3.1))

    print("Drinks:")
    for item in menu.filter_by_category("drinks"):
        print("  ", item)

    print("\nMost popular first:")
    for item in menu.sort_by_popularity():
        print("  ", item)

    order = Order()
    order.add_item(menu.items[0])  # Spicy Burger
    order.add_item(menu.items[1])  # Large Soda
    print("\n", order)

    sam = Customer("Sam")
    print(sam, "verified:", sam.is_verified())
    sam.add_order(order)
    print(sam, "verified:", sam.is_verified())
