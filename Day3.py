print("Welcome to the Amusement Park")

height = int(input("Please Input your Height: "))

if height > 160:
    print("You can Enter the Amusement Park :)")
    age = int(input("Please enter your Age"))
    if age > 18:
        print("You are only need to pay $10")
    elif age >= 15:
        print("You are only need to pay $7")
    else:
        print("You are free to enter the Amusement Park\n Enjoy the Holiday")
elif height >= 155:
    print("Also, I think you are Qualified tho xD")
    age = int(input("Please enter your age "))
    if age <= 16:
        print("You are need to pay $5")
    else:
        print("You are free to enter the Amusement Park")
else:
    print("You are too smoll buddy :( ")