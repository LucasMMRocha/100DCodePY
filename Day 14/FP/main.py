from art import logo
from art import vs
from game_data import data
import random
import os

score = 0

while True:
  
  os.system('cls')
  
  rand_numb_a = random.randint(0, 50)
  rand_numb_b = random.randint(0, 50)

  key_a1 = data[rand_numb_a]['name']
  key_a2 = data[rand_numb_a]['follower_count']
  key_a3 = data[rand_numb_a]['description']
  key_a4 = data[rand_numb_a]['country']
  key_b1 = data[rand_numb_b]['name']
  key_b2 = data[rand_numb_b]['follower_count']
  key_b3 = data[rand_numb_b]['description']
  key_b4 = data[rand_numb_b]['country']
  
  print(f"{logo}")
  
  print(f"Current score: {score}.")

  print(f"Compare A: {key_a1}, a {key_a3}, from {key_a4}")

  print(f"{vs}")

  print(f"Against B: {key_b1}, a {key_b3}, from {key_b4}")
  
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  if data[rand_numb_a]['follower_count'] > data[rand_numb_b]['follower_count'] and answer == 'a':
    score += 1
  
  elif data[rand_numb_b]['follower_count'] > data[rand_numb_a]['follower_count'] and answer == 'b':
    score += 1

  else:
    break