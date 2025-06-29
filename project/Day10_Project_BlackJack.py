import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_scr, computer_scr):
    if user_scr == computer_scr:
        print("Draw!")
    elif user_scr == 0:
        print("You Win")
    elif computer_scr == 0:
        print("You Lose")
    elif user_scr > 21:
        print("You Lose")
    elif computer_scr > 21:
        print("You Win")
    elif user_scr > computer_scr:
        print("You Win")
    else:
        print("You Lose")

def play_game():
    user_card = []
    computer_card = []
    user_score = -1
    computer_score = -1
    game_state = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_state:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your Card {user_card}, Your Score {user_score}")
        print(f"Computer first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_state = True
        else:
            user_choose = input("Please type 'y' to draw a card, or type 'n' to pass:  ")
            if user_choose == "y":
                user_card.append(deal_card())
            else:
                game_state = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your Final Card is {user_card}, and your final score is {user_score}")
    print(f"Computer final card is {computer_card} ana computer final score is {computer_score}")
    print(compare(user_score, computer_score))

print("******Welcome to The Python BlackJack******")
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 10)
    play_game()