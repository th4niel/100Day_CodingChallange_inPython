from calculator_logo import logo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    while_true = True
    print("Welcome to the Pythonista Calculator!")
    print(logo)
    num1 = float(input("Please input the first number: "))

    while while_true:
        for operator in operation:
            print(operator)
        operation_symbol = input("Please choose the opetarion symbol: ")
        num2 = float(input("Please input the second number: "))
        answer = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' if you want to continue calculte with this number {answer} or you can just Type 'new' to start calculate from beginning or also you can stop the program by type 'stop': ")

        if choice == "y":
            num1 = answer
        elif choice == "new":
            while_true = False
            print("\n" *20)
            calculator()
        else:
            exit()
calculator()


"""
PAUSE 1
TODO: Write out the other 3 functions - subtract, multiply and divide.

PAUSE 2
TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

PAUSE 3
TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

Functionality
Program asks the user to type the first number.
Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
Program asks the user to type the second number.
Program works out the result based on the chosen mathematical operator.
Program asks if the user wants to continue working with the previous result.
If yes, program loops to use the previous result as the first number and then repeats the calculation process.
If no, program asks the user for the fist number again and wipes all memory of previous calculations.
Add the logo from art.py
"""
