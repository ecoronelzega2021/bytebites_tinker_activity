# ByteBites backend models
#
# Customer  - a campus user: name + purchase history (list of past Orders)
# FoodItem  - one item we sell: name, price, category, popularity rating
# Menu      - the full list of FoodItems; filters by category and sorts
# Order     - one transaction: the FoodItems a customer picked + the total cost
#
# Classes relate by composition: Menu and Order hold FoodItems, Customer holds Orders.
# No class inherits from another.
