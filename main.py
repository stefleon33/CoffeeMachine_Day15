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

# TODO 3: Print report showing the current resource values when user writes "report". (Water ml, Milk ml, Coffee g, Money $)
"""Function to print the current resources in the machine with units"""
def current_resources():
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

# TODO 5: Process coins.
def payment():
    """Function to collect payment from the customer"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(total)

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
        print("Please insert coins.")
        payment()

# TODO 4: Check resources sufficient?
# TODO 6: Check transaction successful?
# TODO 7: Make Coffee