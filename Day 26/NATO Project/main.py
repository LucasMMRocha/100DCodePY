import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# To do 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# To do 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter your word: ").upper()
letters = [letter for letter in word]

nato_code = [nato_dict.get(letter.upper()) for letter in word]

print(nato_code)
