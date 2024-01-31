from logo import logo
import os

bids = []

def add_bids(name, bid):
  add_person = {}
  add_person[name] = name
  add_person[bid] = bid
  bids.append(add_person)

print(f"{logo}")

print("Welcome to the secret auction program.\n")

should_continue = True

while should_continue:
  name = input("What's your name?: ")
  bid = int(input("what's your bid?: $"))
  more_people = input("Is there any other biders? Type 'yes' or 'no'. ").lower()

  os.system('cls')
  
  add_bids(name, bid)

  highest_bid = 0
  
  for name, bid in bids:
    
    if bid > highest_bid:
      person_name = name
      person_bid = bid
      
    highest_bid = bid
  
  if more_people == 'no':
    should_continue = False

print(f"{person_name}, you won the auction, ${person_bid}")