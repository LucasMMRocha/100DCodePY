#Calculator

from art import logo

#Add
def add(n1, n2):
  return n1 + n2


#Subtract
def sub(n1, n2):
  return n1 - n2


#Multiply
def multi(n1, n2):
  return n1 * n2


#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": multi,
  "/": divide
}



def calculation():

  print(logo)

  num1 = float(input("What is the first number? "))

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:

    operations_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What is the second number? "))

    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operations_symbol} {num2} = {answer}")

    question = input(f"Type 'y' to continue calculating with {answer}, or type'n' to start a new calculation: ").lower()

    if question == 'y':
      num1 = answer
    
    else:
      should_continue = False
      calculation()

calculation()