import sys

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

coin = {'penny': 0.01,
        'dime': 0.10,
        'nickel': 0.05,
        'quarter': 0.25}


# TODO: 2. Function to calculate coins
def coin_input(quarter, dime, nickel, penny):
    quarter *= coin['quarter']
    dime *= coin['dime']
    nickel *= coin['nickel']
    penny *= coin['penny']
    total = quarter + dime + nickel + penny
    price = MENU[coffee]['cost']
    if price > total:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = total - price
        print(f"Here is ${round(change, 2)} in change. Here is your {coffee} ☕️. Enjoy!")


def calculate_resources(coffee):
    if resources['water'] > MENU[coffee]['ingredients']['water']:
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['money'] = MENU[coffee]['cost']
        return True
    print("Sorry there is not enough water.")
    return False


while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    again = calculate_resources(coffee)

    while again:
        # TODO: 1. Print report of all coffee machine resources

        if coffee == 'report':
            for k, v in resources.items():
                print(f"{k}: {v}")
        elif coffee == 'off':
            print("Turning Coffee Machine Off")
            sys.exit()
        elif coffee == 'espresso' or coffee == 'latte' or coffee == 'capuccino':
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))
            coin_input(quarter, dime, nickel, penny)
        else:
            print("Wrong input!")
            break
        break



