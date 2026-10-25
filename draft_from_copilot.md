# ByteBites: First Draft UML (no reference file)

First-pass diagram from an unconstrained prompt: only `bytebites_spec.md` as context and
"Generate a UML class diagram for the ByteBites backend." No ground rules. Kept for comparison
only. Do not build from this.

```mermaid
classDiagram
    class User {
        +int user_id
        +str name
        +str email
        +str password_hash
        +login()
        +logout()
    }
    class Customer {
        +list purchase_history
        +float loyalty_points
        +verify_user()
    }
    class Admin {
        +add_menu_item()
        +remove_menu_item()
    }
    class FoodItem {
        +str name
        +float price
        +str category
        +float popularity_rating
    }
    class Drink {
        +str size
    }
    class Dessert {
        +bool contains_nuts
    }
    class Menu {
        +list items
    }
    class MenuManager {
        +add_item()
        +filter_by_category()
        +sort_by_popularity()
    }
    class Cart {
        +list items
        +add_item()
        +remove_item()
    }
    class Order {
        +int order_id
        +datetime created_at
        +str status
        +calculate_total()
        +apply_discount()
    }
    class Payment {
        +float amount
        +str method
        +process()
    }
    class RecommendationEngine {
        +recommend_pairing()
    }

    User <|-- Customer
    User <|-- Admin
    FoodItem <|-- Drink
    FoodItem <|-- Dessert
    MenuManager --> Menu
    Menu o-- FoodItem
    Customer --> Cart
    Cart --> Order
    Order --> Payment
    RecommendationEngine --> Menu
```

## Problems with this draft

- **12 classes instead of 4.** `User`, `Admin`, `Drink`, `Dessert`, `MenuManager`, `Cart`,
  `Payment`, and `RecommendationEngine` are not in the feature request.
- **Authentication crept in** (`email`, `password_hash`, `login()`, `logout()`). The reference
  file explicitly rules this out.
- **Inheritance where none is needed.** Drinks and desserts are just a `category` value on a
  `FoodItem`. Making them subclasses means a new class every time the menu adds a category.
- **`MenuManager` duplicates `Menu`.** The spec says the collection itself does the filtering.
- **`Cart` and `Order` overlap.** The spec describes one object that holds picked items and
  computes the total. That is `Order`.
- **Extra attributes nobody asked for:** `loyalty_points`, `status`, `created_at`,
  `apply_discount()`, `size`, `contains_nuts`.
- **`RecommendationEngine`** is the feature that suggested soup as dessert. Not in scope.
