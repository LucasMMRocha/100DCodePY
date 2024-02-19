from resourses import MENU
from resourses import resources

should_continue = True


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


total_money = 0

while should_continue:

    drink = input("What would you like? (expresso/latte/cappuccino):")

    print(f"{MENU[drink]["cost"]}")

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

    if drink == 'espresso':
        if total < MENU["espresso"]["cost"]:
            print("Sorry there is not enough money.\nMoney refunded.")
        espresso()
        total_money += MENU["espresso"]["cost"]
        print(f"Here is your espresso, and your change is {change}")

    elif drink == 'latte':
        if total < MENU["latte"]["cost"]:
            print("Sorry there is not enough money.\nMoney refunded.")
        latte()
        total_money += MENU["latte"]["cost"]
        print(f"Here is your latte, and your change is {change}")

    elif drink == 'cappuccino':
        if total < MENU["cappuccino"]["cost"]:
            print("Sorry there is not enough money.\nMoney refunded.")
        cappuccino()
        total_money += MENU["cappuccino"]["cost"]
        print(f"Here is your cappuccino, and your change is {change}")
        print("Sorry")
