import random
from hangman_word import word_list
from hangman_art import stages, logo

live = 6

print(logo)

word_choice = random.choice(word_list)

placeholder = ""

chosen_word = len(word_choice)
for chosen in range(chosen_word):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    print(f"****************************{live}/6 LIVES LEFT****************************")
    guess = input("Please a letter from a - z: ").lower()

    if guess in correct_letter:
        print(f"You already guessed {guess}")
    display = ""

    for letter in word_choice:
        if letter == guess:
            display += letter
            correct_letter.append(guess) #recommended using letter over guess because letter is coming from the original world of choice's
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print("Word to Guess: " + display)

    if guess not in word_choice:
        live -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life!!")

        if live == 0:
            game_over = True
            print("!!!!!!!!!!!!!You Lose!!!!!!!!!!!!!")


    if "_" not in display:
        game_over = True
        print("****************************You Win****************************")

    print(stages[live])

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
#######################################################################################################################
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
#######################################################################################################################
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
#######################################################################################################################
# TODO-1: - Use a while loop to let the user guess again.
# TODO-2: Change the for loop so that you keep the previous correct letters in display.
#######################################################################################################################
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-2: - Update the code below to use the stages List from the file hangman_art.py
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# TODO-6: - Update the code below to tell the user how many lives they have left.
# TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.

