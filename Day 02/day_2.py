# Data Types

# Strings
#print("Hello"[4])


# Integer
#print(123 + 345)
#print(1_101)


# Float
#3.14159


# Boolean
#True
#False

# Conversion

num_char = len(input("What's is your name?"))

#print("Your name contais " + num_char + " characters")

#The code above will not work, we need to convert the input into a string

new_num_char = str(num_char)
print("Your name contais " + new_num_char + " characters")

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))


# PEMDASLR
#()
#**
#* /
#+ -


# Rounded Numbers

round(8 / 3, 2)
# The code above will round the result for the first 2 decimals

#+=
#-=
#/=
#*=

score = 3
height = 1.75
isWinning = True

print(f"The score is {score}. Your height is {height}. You are winning {isWinning}")