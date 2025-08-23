from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#search password
def search_password():
    website = website_entry.get()
    try:
        with open("./password-manager/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists!")



#Set random generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #   password += char

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you havent left any field empty!")
    else:
        try:
            with open("./password-manager/data.json", "r") as data_file: #"w"=dump, "r"=load, "a"=
                #Reading
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./password-manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 3)
        else:
            #Update
            data.update(new_data)
            # print(data)

            with open("./password-manager/data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=3)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canva = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./password-manager/logo.png")
canva.create_image(100,100, image=logo_img)
canva.grid(row=0, column=1,)

#Label
website_label = Label(text="Website")
website_label.grid(row = 1, column = 0)
email_label = Label(text="Email/Username: ")
email_label.grid(row = 2, column = 0)
password_label = Label(text="Password: ")
password_label.grid(row = 3, column = 0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, padx=3, pady=3)
website_entry.focus()
email_entry = Entry(width=30)
email_entry.grid(row=2, column=1, columnspan=1, padx=3, pady=3)
email_entry.insert(0, "example@email.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, padx=3, pady=3)

#Button
search_button = Button(text="Search", width=19, command=search_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password",width=19, command=generate_password)
generate_password_button.grid(row=3, column=2, padx=3, pady=3)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()