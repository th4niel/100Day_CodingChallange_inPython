print("Welcome to the Python rollercoaster! ")

height = int(input("Please input your height: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))
    if age < 12:
        bill += 5
    elif age <=17:
        bill += 7
    elif 45 <= age <= 55:  #this condition  "45 <= age <= 55" (from a until b) || #2 age >= 45 and age <= 55
        bill += 0
    else:
        bill += 12
    print(f"Your Ticket Price right now is ${bill}")

    want_photo = input("Do you want photo? Y or N: ")

    if want_photo == "Y":
        bill += 3
    else:
        bill += 0

    print(f"Your total bill is ${bill}")

else:
    print("Cant ride, you are too smol")


