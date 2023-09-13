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


def check_resources(drink_ing):
    for item in drink_ing:
        if drink_ing[item] >= resources[item]:
            print(f"Not enough {item}. Sorry!")
            return False
        return True


def check_amount():
    print("Please enter the number of coins of each type you have:")
    amount = int(input("How many quarters do you have? : ")) * 0.25
    amount += int(input("How many dimes do you have? : ")) * 0.10
    amount += int(input("How many nickels do you have? : ")) * 0.05
    amount += int(input("How many pennies do you have? : ")) * 0.01
    return amount


def deduct_resources(drink_ing):
    for item in drink_ing:
        resources[item] -= drink_ing[item]

    return resources


done_making_drink = False
drink = {}
profit = 0
while not done_making_drink:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "off":
        done_making_drink = True
    elif coffee == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[coffee]
        if check_resources(drink["ingredients"]):
            total = check_amount()
            if total < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                done_making_drink = True
            else:
                profit += drink["cost"]
                change = round(total - drink["cost"], 2)
                print(f"Here is ${change} dollars in change.")
                resources = deduct_resources(drink["ingredients"])
                print(f"Here is your {coffee}. ☕️ Enjoy! ")
