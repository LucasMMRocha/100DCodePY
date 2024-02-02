import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number beween 1 and 100.\n")

number = random.randint(1, 100)

difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
  guesses = 10
  
elif difficulty == 'hard':
  guesses = 5

while guesses != 0:
  print(f"You have {guesses} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  guesses -= 1
  
  if guess > number:
    print("Too high.\nGuess again.")
    
  elif guess < number:
    print("Too low.\nGuess again.")
  
  if guess == number:
    print(f"You got it! The answer was {number}.")
    break