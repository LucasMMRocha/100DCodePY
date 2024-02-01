#from art import logo
import random
import os

def add(c1, list):
  list.append(c1)

def total(list):
  return sum(list)
  
logo = """
 .------.            _ n    _            _    _            _    
 |A_  _ |.          | |   | |          | |  (_)          | |   
 |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
 | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
 `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
       |  \/ K|                            _/ |                
       `------'                           |__/           
 """

#Black Jack Game

should_continue = True

while should_continue == True:

  question = input("Do you want to play a Black Jack game? 'y' for yes and 'n' for no: ").lower()

  os.system('clear')

  if question == 'n':
    should_continue = False

  if question == 'y':

    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    cards_p1 = []
    cards_cp = []

    x = 0
    for x in range(2):
      card_p1 = cards[random.randint(0, 12)]
      card_cp = cards[random.randint(0, 12)]
      add(card_p1, cards_p1)
      add(card_cp, cards_cp)

    print(f"Your cards are [{cards_p1}], current score: {total(cards_p1)}")
    print(f"Computer's first card: {cards_cp[0]}\n")

    while total(cards_p1) < 21:

      card_p1 = cards[random.randint(0, 12)]

      if total(cards_cp) < 17:
        card_cp = cards[random.randint(0, 12)]
        add(card_cp, cards_cp)

      question_2 = input("Type 'y' to get another card, type 'n' to pass: ")
      
      if question_2 == 'n':
        break

      card_p1 = cards[random.randint(0, len(cards))]

      add(card_p1, cards_p1)
      
      

      print(f"Your cards are {cards_p1}, current score: {total(cards_p1)}")
      print(f"Computer's first card: {cards_cp[0]}\n")
    
    print(f"Your final hand: {cards_p1}, final score: {total(cards_p1)}")
    print(f"Computer's final hand: {cards_cp}, final score: {total(cards_cp)}")
    if total(cards_p1) <= 21 and total(cards_p1) < total(cards_cp):
      print("You won!")
    elif total(cards_cp) <= 21 and total(cards_cp) > total(cards_p1):
      print("You lost.")
    elif total(cards_p1) == total(cards_cp):
      print("DRAW")
    else:
      print("You went over. You lost...")