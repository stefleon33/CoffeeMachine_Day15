MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# TODO 3: Print report showing the current resource values when user writes "report". (Water ml, Milk ml, Coffee g, Money $)
def current_resources():
    """Function to print the current resources in the machine with units"""
    for resource, amount in resources.items():
        if resource == "water":
            unit = "ml"
        elif resource == "milk":
            unit = "ml"
        elif resource == "coffee":
            unit = "g"
        else:
            unit = ""
        print(f"{resource.capitalize()}: {amount}{unit}")
    print(f"Money: ${profit}")

# TODO 5: Process coins.
def process_coins():
    """Function to collect payment from the customer"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

# TODO 6: Check transaction successful?
def is_transaction_successful(money_paid, beverage_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_paid >= beverage_cost:
        change = round(money_paid - beverage_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += beverage_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# TODO 4: Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    """If the customer orders a drink, the machine needs to check if there are enough resources available."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# TODO 7: Make Coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} ☕️. Enjoy!")

coffe_machine_on = True
while coffe_machine_on is True:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt. (code should end)
    if order == "off":
        print("Good bye!")
        coffe_machine_on = False
    elif order == "report":
        current_resources()
        continue
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment= process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
