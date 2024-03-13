# For loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# List Comprehension

# new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]

name = "Lucas"
letters_list = [letter for letter in name]

range_list = [num * 2 for num in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]

long_names = [name.upper() for name in names if len(name) > 5]


