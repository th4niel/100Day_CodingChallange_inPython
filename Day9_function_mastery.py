def my_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Y DONT INPUT ANYTHINGGGGG"

    first_name = f_name.title()
    second_name = l_name.title()
    combined = first_name +second_name
    return f"{combined}"

print(my_name(input("What your name: "), input("What is your name: ")))