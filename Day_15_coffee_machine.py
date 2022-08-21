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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

# TODO : Report the user what the available resource the machine have
# TODO : define function that checks the available resource
# TODO : ask the user to insert coin and calculate the price if customer has change
# TODO : ask user preference
profit = 0


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {resources[item]}")
            return False
    return True


def payment_method():
    print("Please insert the coins ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_payment_successful(money_received, actual_cost):
    if money_received > actual_cost:
        change = round(money_received - actual_cost, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit += actual_cost
        return True
    else:
        print("Sorry you haven't inserted enough money . Money refunded.")
        return False


def make_coffee(order_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy you {order_name} , Thanks for choosing us!")


coffee_machine_on = True

while coffee_machine_on:
    print("Welcome to YGCoffee")
    print("Press 'off' to close the machine")
    print("Press 'report' to check the available resource")

    choice = input("What would you like? (espresso / latte / cappuccino ):")
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        print(f"Water:  {resources['water']}ml.")
        print(f"Milk:   {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            paid = payment_method()
            if is_payment_successful(paid, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





