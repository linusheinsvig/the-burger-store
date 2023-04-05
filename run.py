print("Welcome to The Burger Store")
print("Can I please take your order?\n")

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

while True:
    try:
        burger_order = int(input("\nEnter the number of the burger you would like to order (1-5): "))
        if burger_order not in burgers:
            raise ValueError("Please enter a number thats on the menu")
        order, price = burgers[burger_order]
        print(f"You ordered the {order} burger, which costs ${price:.2f}.\n")
        break
    except ValueError as error:
        print("Please enter a number thats on the menu")

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

while True:
    try:
        extras_order = int(input("\nEnter the number of the extras you would like to order (1-3): "))
        if extras_order not in extras:
            raise ValueError("Please enter a number thats on the menu")
        order, price = extras[extras_order]
        print(f"You choose to add {order} to your burger, which costs ${price:.2f}.\n")
        break
    except ValueError as error:
        print("Please enter a number thats on the menu")

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

while True:
    try:
        sides_order = int(input("\nEnter the number of the sides you would like to order (1-4): "))
        if sides_order not in sides:
            raise ValueError("Please enter a number thats on the menu")
        order, price = sides[sides_order]
        print(f"You choose to add {order} to your order, which costs ${price:.2f}.\n")
        break
    except ValueError as error:
        print("Please enter a number thats on the menu")

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

while True:
    try:
        drinks_order = int(input("\nEnter the number of the drink you would like to order (1-4): "))
        if drinks_order not in drinks:
            raise ValueError("Please enter a number thats on the menu")
        order, price = drinks[drinks_order]
        print(f"You choose to add {order} to your order, which costs ${price:.2f}.\n")
        break
    except ValueError as error:
        print("Please enter a number thats on the menu")

"""
Calculating total price
"""
total = burgers[burger_order][1] + extras[extras_order][1] + sides[sides_order][1] + drinks[drinks_order][1]
print(f"The total cost of your order is ${total:.2f}.")
