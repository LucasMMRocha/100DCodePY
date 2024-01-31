#  Final Project (Tip calculator)

print("Welcome to tip calculator./n")
bill = input("What is the total bill? $")
tip_amount = input("what percentage tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")

percentage = float(bill) * (int(tip_amount) / 100)
total_bill = percentage + float(bill)
result = round(total_bill / int(number_of_people), 2)

print(f"Each person should pay {result}")