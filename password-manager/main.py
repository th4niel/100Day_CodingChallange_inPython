from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you havent left any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"       
                                    f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:     
            with open("./password-manager/data.txt", "a") as data_file:
                data_file.write(f"{website}  | {email} | {password}\n")
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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, padx=3, pady=3)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=3, pady=3)
email_entry.insert(0, "example@email.com")
password_entry = Entry(width=16)
password_entry.grid(row=3, column=1, padx=3, pady=3)

#Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=3, pady=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()