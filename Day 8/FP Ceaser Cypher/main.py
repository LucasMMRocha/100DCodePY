from logo import logo
from function import ceaser

print(f"{logo}")
should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  
  ceaser(direction, text, shift)
  answer = input("Do you want to do it again?\n").lower()
  if answer == 'no':
    should_continue = False