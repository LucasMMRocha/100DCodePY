#Step 4

from hangman_art import stages
from hangman_words import word_list
import os
import random


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guessed_letters = []

#TODO-1: - Create a variable called 'lives' to keep track of the
#number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    #TODO-4: - If the user has entered a letter they've already
    #guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter:
        #{letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

  
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n{stages[lives]}")
        #TODO-5: - If the letter is not in the chosen_word, print
        #out the letter and let them know it's not in the word.
    elif guess in guessed_letters:
      print(f"You already guessed {guess}, try another one.\n{stages[lives]}")
        
    else:
        print(f"You guessed {guess}, {stages[lives]}")

    guessed_letters.append(guess)
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should
    #print "You lose."
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if lives == 0:
        print("You lose")
        end_of_game = True
    if "_" not in display:
        end_of_game = True
        print(f"You win.")
    #TODO-3: - print the ASCII art from 'stages' that corresponds to
    #the current number of 'lives' the user has remaining.