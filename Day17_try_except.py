try:
    age = int(input("Please enter your Age: "))
except ValueError:
    print("Please enter a value number such as 10")
    age = int(input("Please enter your Age: "))

if age > 18:
    print(f"you are {age} years old capable to get the Driving License")
else:
    print(f"You are {age} years old, still too young")