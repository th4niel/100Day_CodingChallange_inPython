from Day18_gameData import data
import random
from higherLower_art import logo, vs


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name} is a {account_desc}, from {account_country}"

def check_answ(user_guess,a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

print(logo)

score = 0 
account_b = random.choice(data)
game_status = True


while game_status:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has moer followers? Type 'A' or 'B': ").lower()

    print("\n" *20)
    print(logo)

    a_followerCount = account_a["follower_count"]
    b_followerCount = account_b["follower_count"]

    is_correct = check_answ(guess, a_followerCount, b_followerCount)

    if is_correct:
        score += 1
        print(f"You are Right! your current score is {score}")
    else:
        print(f"Sorry you got the wrong answer!, Final score = {score}")
        game_status = False