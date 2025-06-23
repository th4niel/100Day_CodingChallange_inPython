import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Online Python Password Generator Website!")

rn_letter = int(input("Please input how many Letters would you like in your password: "))
rn_number = int(input("Please input how many Numbers would you like in your password: "))
rn_symbol = int(input("Please input how many Symbols would you like in your password: "))

password_list = []

for char in range(1, rn_letter +1):
    password_list += random.choice(letters)
for char in range(1, rn_number +1):
    password_list += random.choice(numbers)
for char in range(1, rn_symbol +1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Here it is your warm Crispy Password! fresh from the Python oven 🔥🔥: {password}")