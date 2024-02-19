from resourses import MENU
from resourses import resources

is_on = True


def espresso():
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]


def latte():
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]


def cappuccino():
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]


while is_on:

    drink = input("What would you like? (espresso/latte/cappuccino):")
    
    if drink == 'off':
        is_on = False
    
    elif not drink == 'report':
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water.")

        elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")

        if not drink == 'espresso':
            if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")

        print("Please insert coins.")

        quarters = int(input("how many quarters?"))
        dimes = int(input("how many dimes?"))
        nickles = int(input("how many nickels?"))
        pennies = int(input("how many pennies?"))

        total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)

        change = total - MENU[drink]["cost"]
        change_rounded = round(change, 2)
        
        if drink == 'espresso':
            if total < MENU["espresso"]["cost"]:
                print("Sorry there is not enough money.\nMoney refunded.")
            else:
                espresso()
                resources["money"] += MENU["espresso"]["cost"]
                print(f"Here is your espresso, and your change is {change_rounded}")

        elif drink == 'latte':
            if total < MENU["latte"]["cost"]:
                print("Sorry there is not enough money.\nMoney refunded.")
            else:
                latte()
                resources["money"] += MENU["latte"]["cost"]
                print(f"Here is your latte, and your change is {change_rounded}")

        elif drink == 'cappuccino':
            if total < MENU["cappuccino"]["cost"]:
                print("Sorry there is not enough money.\nMoney refunded.")
            else:
                cappuccino()
                resources["money"] += MENU["cappuccino"]["cost"]
                print(f"Here is your cappuccino, and your change is {change_rounded}")
                print("Sorry")
    else:
        print(f"{resources["water"]}")
        print(f"{resources["milk"]}")
        print(f"{resources["coffee"]}")
        print(f"{resources["money"]}")