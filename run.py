print("Welcome to The Burger Store")
print("Can I please take your order?")

"""
Burger menu and ordering function
"""

burgers = {
    1: ("Original", 8),
    2: ("Cheeze", 9),
    3: ("Mexicana", 10),
    4: ("Paris", 10),
    5: ("Vegi", 9),
}

print("Burgers:")
for i, (item, price) in burgers.items():
    print(f"{i}. {item}: ${price:.2f}")

burger_order = int(input("Enter the number of the burger you would like to order (1-5): "))

if burger_order in burgers:
    order, price = burgers[burger_order]
    print(f"You ordered the {order} burger, which costs ${price:.2f}.")
else:
    print("Sorry, that item is not on the menu.")

"""
Extras menu and choise
"""

extras = {
    1: ("Bacon", 2),
    2: ("Cheese", 2),
    3: ("Extra Meat", 5),
}

print("Would you like to add something to your burger?:")
for i, (item, price) in extras.items():
    print(f"{i}. {item}: ${price:.2f}")

extras_order = int(input("Enter the number of the extras you would like to order (1-3): "))

if extras_order in extras:
    order, price = extras[extras_order]
    print(f"You choose to add {order} to your burger, which costs ${price:.2f}.")
else:
    print("Sorry, that item is not on the menu.")

"""
Menu and chooise of sides
"""
sides = {
    1: ("Fries", 3),
    2: ("Sweet Potato Fries", 3),
    3: ("Onion Rings", 4),
    4: ("Chili Cheese", 4),
}

print("Would you like to add any sides to your order?:")
for i, (item, price) in sides.items():
    print(f"{i}. {item}: ${price:.2f}")

sides_order = int(input("Enter the number of the side you would like to order (1-4): "))

if sides_order in sides:
    order, price = sides[sides_order]
    print(f"You choose to add {order} to your order, which costs ${price:.2f}.")
else:
    print("Sorry, that item is not on the menu.")

"""
Drinks Menu
"""
drinks = {
    1: ("Soda", 2),
    2: ("Water", 1),
    3: ("Milk", 2),
    4: ("Orange Juice", 3),
}

print("Would you like something to drink?:")
for i, (item, price) in drinks.items():
    print(f"{i}. {item}: ${price:.2f}")

drinks_order = int(input("Enter the number of the drink you would like to order (1-4): "))

if drinks_order in drinks:
    order, price = drinks[drinks_order]
    print(f"You choose to add {order} to your order, which costs ${price:.2f}.")
else:
    print("Sorry, that item is not on the menu.")

"""
Calculating total price
"""
total = burgers[burger_order][1] + extras[extras_order][1] + sides[sides_order][1] + drinks[drinks_order][1]
print(f"The total cost of your order is ${total:.2f}.")
