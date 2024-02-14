# Flavors

# Expresso        Latte         Cappuccino
# W - 50ml       W - 200ml       W - 250ml
# C - 18g         C - 24g         C - 24g
#                M - 150ml       M - 100ml

#   $1.50          $2.50           $3.00

from resourses import MENU
from resourses import resources

total_money = 0
should_continue = True

def espresso():
  global total_money
  resources["water"] -= MENU["espresso"]["ingredients"]["water"]
  resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
  total_money += 1.50

  
def latte():
  global total_money
  resources["water"] -= MENU["latte"]["ingredients"]["water"]
  resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
  resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
  total_money += 2.50
  
def cappuccino():
  global total_money
  resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
  resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
  resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
  total_money += 3.00

  
while should_continue:
  
  drink = input("What would you like? (espresso/latte/cappuccino):").lower()
  
  if drink == 'espresso':
    espresso()
    
  elif drink == 'latte':
    latte()
  
  elif drink == 'cappuccino':
    cappuccino()
    if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
      print("Sorry there is not enough milk.")
      
  if resources["water"]  < MENU[drink]["ingredients"]["water"]:
    print("Sorry there is not enough water.")
  
  elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
    print("Sorry there is not enough coffee.")
    
  
    
  print("Please insert coins.")

  quarters = 0.25
  dimes = 0.1
  nickles = 0.05
  pennies = 0.01

  quarters *= int(input("how many quarters?"))
  dimes *= int(input("how many dimes?"))
  nickles *= int(input("how many nickels?"))
  pennies *= int(input("how many pennies?"))
  
  total = quarters + dimes + nickles + pennies
  
  change = total - MENU[drink]["cost"]
  
  if total < MENU[drink]["cost"]:
    print("Sorry there is not enough money.\nMoney refunded.")