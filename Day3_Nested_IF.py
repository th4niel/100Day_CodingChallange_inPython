print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age right now? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age > 18:
        print("You need to pay $100")
    else:
        print("and you are free to enter")
else:
    print("Sorry you have to grow taller before you can ride.")
