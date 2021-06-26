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

money = 0


def check_resources(coffee_name):
    if coffee_name in MENU:
        for ingredient in resources:
            if ingredient in MENU[coffee_name]["ingredients"]:
                if MENU[coffee_name]["ingredients"][ingredient] > resources[ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    return False
        return True


def make_coffee(coffee_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name} ☕️. Enjoy!")


def check_coins(coffee_name):
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total_sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    cost_coffee = MENU[coffee_name]["cost"]
    if total_sum >= cost_coffee:
        global money
        money += cost_coffee
        change = round(total_sum - cost_coffee, 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


coffee_machine_work = True

while coffee_machine_work:
    user_answer = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if user_answer in MENU:
        if check_resources(user_answer):
            if check_coins(user_answer):
                make_coffee(user_answer, MENU[user_answer]["ingredients"])
    elif user_answer == "off":
        coffee_machine_work = False
    elif user_answer == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${money}")
    else:
        print('Sorry, unknown command')
