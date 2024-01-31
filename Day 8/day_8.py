# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#   print("Hi")
#   print("How")
#   print("You do'in?")

# greet()

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How are you doing {name}")

# greet_with_name("Lucas")

#Functions with more than 1 input

# def greet_with(name = "Lucas", location = "Nowhere"):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}")

# greet_with()

# Write your code below this line 👇

import math

def paint_calc(height, width, cover):
  cans = math.ceil((height * width)/cover)
  print(f"{cans}")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)