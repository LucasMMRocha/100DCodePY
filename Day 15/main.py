# Flavors

# Expresso        Latte         Cappuccino
# W - 50ml       W - 200ml       W - 250ml
# C - 18g         C - 24g         C - 24g
#                M - 150ml       M - 100ml

#   $1.50          $2.50           $3.00

from resourses import MENU
from resourses import resorses
total_money = 0
should_continue = True

def espresso():
  resorses["water"] -= MENU[0][0]["water"]
  resorses["coffee"] -= MENU[0][0]["coffee"]
  total_money += 1.50

  
def latte():
  resorses["water"] -= MENU[1][0]["water"]
  resorses["coffee"] -= MENU[1][0]["coffee"]
  resorses["milk"] -= MENU[1][0]["milk"]
  total_money += 2.50
  
def cappuccino():
  resorses["water"] -= MENU[2][0]["water"]
  resorses["coffee"] -= MENU[2][0]["coffee"]
  resorses["milk"] -= MENU[2][0]["milk"]
  total_money += 3.00
  
while should_continue:

  drink = input("What would you like? (expresso/latte/cappuccino):")
  
  if resorses["water"]  < MENU[drink][0]["water"]:
    print("Sorry there is not enough water.")
  
  if resorses["coffe"] < MENU[drink][0]["coffee"]:
    print("Sorry there is not enough coffee.")
    
  if resorses["milk"] < MENU[drink][0]["milk"]:
    print("Sorry there is not enough milk.")
    
  print("Please insert coins.")

  quarters = int(input("how many quarters?"))
  dimes = int(input("how many dimes?"))
  nickles = int(input("how many nickels?"))
  pennies = int(input("how many pennies?"))
  
  total = quarters + dimes + nickles + pennies
  
  if total < MENU[drink][1]:
    print("Sorry there is not enough money.\nMoney refunded.")