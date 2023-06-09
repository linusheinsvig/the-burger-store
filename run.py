print("Welcome to The Burger Store")

# Burger Menu
burgers = {
    0: ("No thanks", 0),
    1: ("Original Burger", 8),
    2: ("Cheeze Burger", 9),
    3: ("Mexicana Burger", 10),
    4: ("Chicken Burger", 9),
    5: ("Vegi Burger", 9),
    }

# Extras Menu
extras = {
    0: ("No thanks", 0),
    1: ("Bacon", 2),
    2: ("Cheese", 2),
    3: ("Extra Meat", 5),
    }

# Sides Menu
sides = {
    0: ("No thanks", 0),
    1: ("Fries", 3),
    2: ("Sweet Potato Fries", 3),
    3: ("Onion Rings", 4),
    4: ("Chili Cheese", 4),
    }

# Drinks Menu
drinks = {
    0: ("No thanks", 0),
    1: ("Soda", 2),
    2: ("Water", 1),
    3: ("Milk", 2),
    4: ("Orange Juice", 3),
}

while True:
    # Empty list to store user's choices
    choices = []
    # Users shopping cart
    total_cost = 0

    start = input("Do you want to place an order? (y/n): \n")
    if start.lower() == "n":
        print("Thank you for stopping by!")
        break
    elif start.lower() != "y":
        print("Invalid input. Please enter Y or N.")
        continue
    while True:
        print("What kind of burger would you like?\n")

        # Displaying burger choices
        print("Burgers:")
        for i, (item, price) in burgers.items():
            print(f"{i}. {item}: ${price:.2f}")

        # Checking if choice is valid
        while True:
            try:
                burger_order = int(input(
                    "Enter the number of the burger you would like (0-5):\n"))
                if burger_order not in burgers:
                    raise ValueError("Please enter a number thats on the menu")
                order, price = burgers[burger_order]
                print(
                    f"You ordered the {order} burger, costing ${price:.2f}")
                break
            except ValueError as error:
                print("Please enter a number thats on the menu")

        # Add the burger choice to the list
        burger_choice = burgers[burger_order][0]
        choices.append(burger_choice)

        # Add burger to the total cost
        total_cost += burgers[burger_order][1]

        # Displaying extras choices
        print("Would you like to add something to your burger?")
        for i, (item, price) in extras.items():
            print(f"{i}. {item}: ${price:.2f}")

        # Checking if choice is valid
        while True:
            try:
                extras_order = int(input(
                    "Enter the number you would like to order (0-3):\n "))
                if extras_order not in extras:
                    raise ValueError("Please enter a number thats on the menu")
                order, price = extras[extras_order]
                print(f"You choose to add {order} costsing ${price:.2f}.\n")
                break
            except ValueError as error:
                print("Please enter a number thats on the menu")

        # Add the extras choice to the list
        extras_choice = extras[extras_order][0]
        choices.append(extras_choice)

        # Add extras to the total cost
        total_cost += extras[extras_order][1]

        # Displaying sides choices
        print("Would you like any side orders?")
        for i, (item, price) in sides.items():
            print(f"{i}. {item}: ${price:.2f}")

        # Checking if choice is valid
        while True:
            try:
                sides_order = int(input(
                    "Enter the number you would like to order (0-4):\n "))
                if sides_order not in sides:
                    raise ValueError("Please enter a number thats on the menu")
                order, price = sides[sides_order]
                print(f"You choose to add {order} costing ${price:.2f}.\n")
                break
            except ValueError as error:
                print("Please enter a number thats on the menu")

        # Add the sides choice to the list
        sides_choice = sides[sides_order][0]
        choices.append(sides_choice)

        # Add sides to the total cost
        total_cost += sides[sides_order][1]

        # Displaying drinks choices
        print("Would you like something to drink?")
        for i, (item, price) in drinks.items():
            print(f"{i}. {item}: ${price:.2f}")

        # Checking if choice is valid
        while True:
            try:
                drinks_order = int(input(
                    "Enter the number you would like to order (0-4):\n"))
                if drinks_order not in drinks:
                    raise ValueError("Please enter a number thats on the menu")
                order, price = drinks[drinks_order]
                print(f"You choose to add {order} costing ${price:.2f}.\n")
                break
            except ValueError as error:
                print("Please enter a number thats on the menu")

        # Add the drinks choice to the list
        drinks_choice = drinks[drinks_order][0]
        choices.append(drinks_choice)

        # Add drinks to the total cost
        total_cost += drinks[drinks_order][1]

        # Print the user's choices
        print(
            f"You ordered: {burger_choice} with extra {extras_choice},"
            f"{sides_choice} on the side and {drinks_choice} to drink\n")

        # Print the total cost for the user
        print(f"The total cost of your order is ${total_cost:.2f}.")

        # Asks the user if they would like to add something more
        add_more = input(
            "Would you like to add more items to your order? (y/n):\n ")
        if add_more.lower() == "n":
            print("Thank you for your order, your food is beeing prepared!")
            break
        elif add_more.lower() == "y":
            print("Sure, let's add more items!\n")
        else:
            print("Please enter yes or no y/n")
