burgers = {
    1: ("Original", 8),
    2: ("Cheeze", 9),
    3: ("Mexicana", 10),
    4: ("Paris", 10),
    5: ("Vegi", 9),
}

print("Menu:")
for i, (item, price) in burgers.items():
    print(f"{i}. {item}: ${price:.2f}")

burger_order = int(input("Enter the number of the burger you would like to order (1-5): "))

if burger_order in burgers:
    order, price = burgers[burger_order]
    print(f"You ordered the {order} burger, which costs ${price:.2f}.")
else:
    print("Sorry, that item is not on the menu.")


extras = {
    "Bacon": 2,
    "Cheese": 2,
    "Extra Meat": 5,
}


sides = {
    "Fries": 3,
    "Sweet Potato Fries": 3,
    "Onion Rings": 4,
    "Chili Cheese": 4,
}

drinks = {
    "Soda": 2,
    "Water": 1,
    "Milk": 2,
    "Orange Juice": 3,
}


