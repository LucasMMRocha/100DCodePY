import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you chose? 0 for Rock, 1 for Paper or 2 for Scissors.")
comp_choice = random.randint(0, 2)

game = [rock, paper, scissors]

choice_number = int(choice)

if choice_number < 0 or choice_number > 2:
  print("Invalid input! Please, try again.")
else:
  if comp_choice == choice_number:
    print(f"{game[choice_number]}\nComputer choice:\n{game[comp_choice]}\nDraw\n\n-")
  
  if comp_choice == 0 and choice_number == 1:
    print(f"{game[choice_number]}\nComputer choice:\n{game[comp_choice]}\nYou won!\n\n-")
  
  if comp_choice == 0 and choice_number == 2:
    print(f"{game[choice_number]}\nComputer choice:\n{game[comp_choice]}\nYou lose...\n\n-")
  
  if comp_choice == 1 and choice_number == 0:
    print(f"{game[choice_number]}\nComputer choice:\n{game[comp_choice]}\nYou lose...\n\n-")
  
  if comp_choice == 1 and choice_number == 2:
    print(f"{game[choice_number]}\nComputer choice:\n{game[comp_choice]}\nYou won!\n\n-")
  
  if comp_choice == 2 and choice_number == 0:
    print(f"{game[choice_number]}\nComputer choice:\n{game[comp_choice]}\nYou won!\n\n-")
  
  if comp_choice == 2 and choice_number == 1:
    print(f"{game[choice_number]}\nComputer choice:\n{game[comp_choice]}\nYou lose...\n\n-")