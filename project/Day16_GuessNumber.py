from random import randint

easy_level = 10
hard_level = 5

def check_answer(user_guess, actual_answ, turns):
    if user_guess > actual_answ:
        print("Your answer just too High!")
        return turns - 1
    elif user_guess < actual_answ:
        print("Your answer just too Low!")
        return turns - 1
    else:
        print(f"Congratulation,the number is: {actual_answ}, You are guessing the right number!")
        return turns



def set_level():
   level = input("Please select level between easy or hard: ").lower()
   if level == "easy":
       return easy_level
   else:
       return hard_level
   


def game_on():
    print("Welcome to the Guessing Number GAME")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_level()
    guess = 0

    while guess != answer:
        print(f"You have {turns} live remainings")

        try:
            guess = int(input("Make a guess: "))

            if guess < 1 or guess >= 101:
                print("Please enter a number between 1 and 100!")
                continue

        except ValueError:
                print("Please enter a valid number")
                continue
        
        turns = check_answer(guess, answer, turns)

        if guess != answer and turns > 0:
            print("Guess again!")

        elif turns == 0:
            print("You Lose!")

game_on()