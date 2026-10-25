import pytest

from models import Customer, FoodItem, Menu, Order


@pytest.fixture
def menu():
    m = Menu()
    m.add_item(FoodItem("Spicy Burger", 10.00, "Mains", 4.6))
    m.add_item(FoodItem("Large Soda", 5.00, "Drinks", 3.8))
    m.add_item(FoodItem("Cold Brew", 4.25, "Drinks", 4.9))
    m.add_item(FoodItem("Chocolate Chip Cookie", 2.50, "Desserts", 4.4))
    return m


# ---------- Order totals ----------

def test_calculate_total_with_multiple_items():
    # A $10 burger and a $5 soda should total $15.
    order = Order()
    order.add_item(FoodItem("Spicy Burger", 10.00, "Mains", 4.6))
    order.add_item(FoodItem("Large Soda", 5.00, "Drinks", 3.8))
    assert order.calculate_total() == 15.00


def test_order_total_is_zero_when_empty():
    # An order with nothing in it costs $0 and does not crash.
    assert Order().calculate_total() == 0.0


def test_total_has_no_floating_point_leftovers():
    # 0.10 + 0.20 should come out as 0.30, not 0.30000000000000004.
    order = Order()
    order.add_item(FoodItem("Mint", 0.10, "Desserts", 3.0))
    order.add_item(FoodItem("Gum", 0.20, "Desserts", 3.0))
    assert order.calculate_total() == 0.30


def test_same_item_twice_counts_twice():
    # Ordering two sodas charges for two sodas.
    soda = FoodItem("Large Soda", 5.00, "Drinks", 3.8)
    order = Order()
    order.add_item(soda)
    order.add_item(soda)
    assert order.calculate_total() == 10.00


# ---------- Menu filtering ----------

def test_filter_by_category_returns_only_that_category(menu):
    # Filtering "Drinks" returns the two drinks and nothing else.
    drinks = menu.filter_by_category("Drinks")
    assert [item.name for item in drinks] == ["Large Soda", "Cold Brew"]


def test_filter_by_category_ignores_case_and_spaces(menu):
    # "  drinks " finds the same items as "Drinks".
    assert len(menu.filter_by_category("  drinks ")) == 2


def test_filter_by_unknown_category_returns_empty_list(menu):
    # A category with no items gives an empty list, not an error.
    assert menu.filter_by_category("Sushi") == []


# ---------- Menu sorting ----------

def test_sort_by_popularity_puts_highest_rating_first(menu):
    # Items come back from most to least popular.
    ratings = [item.popularity_rating for item in menu.sort_by_popularity()]
    assert ratings == [4.9, 4.6, 4.4, 3.8]


def test_sort_by_popularity_does_not_change_menu_order(menu):
    # Sorting returns a new list and leaves the menu as it was.
    before = [item.name for item in menu.items]
    menu.sort_by_popularity()
    assert [item.name for item in menu.items] == before


# ---------- Customers ----------

def test_new_customer_is_not_verified():
    # Someone with no purchase history is not yet a verified user.
    assert Customer("Sam").is_verified() is False


def test_customer_is_verified_after_an_order():
    # One past order is enough to count as a real user.
    sam = Customer("Sam")
    sam.add_order(Order())
    assert sam.is_verified() is True
    assert len(sam.purchase_history) == 1


def test_customers_do_not_share_purchase_history():
    # Adding an order to one customer does not show up on another.
    a, b = Customer("A"), Customer("B")
    a.add_order(Order())
    assert len(b.purchase_history) == 0
