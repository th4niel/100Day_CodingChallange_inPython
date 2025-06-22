import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
print("Welcome to the Rock, Paper & Scissor by Python")
user_input =int(input("Please Choose your Choices 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors': "))
if user_input < 0 or user_input > 2:
    print("❌ Invalid choice! Please input 0 for Rock, 1 for Paper, or 2 for Scissors.")
    exit() #exit() is used to stop the program immediately,
print(f"You Choose:\n {images[user_input]}")
computer_choice = random.randint(0, 2 )
print(f"Computer Choose:\n {images[computer_choice]}")

if user_input == computer_choice:
    print("⚔️ Game D.R.A.W ⚔️")
# Break the long logical condition into multiple lines using backslash (\)
elif (user_input == 0 and computer_choice == 2) or \
     (user_input == 1 and computer_choice == 0) or \
     (user_input == 2 and computer_choice == 1):
    print("🏆 YOU WIN 🏆")
else:
    print("You LOSE 😢😢😢")
    
