from tkinter import *

window = Tk()
window.title("Hello")
window.minsize(width=600, height=400)

my_label = Label(text="Hello", font=("Arial", 25, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    new_text = entry_text.get() #Entry class
    my_label.config(text=new_text)

button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="click me", command=button_clicked)
new_button.grid(column=2, row=0)

entry_text = Entry(width=10)
entry_text.grid(column=3, row=2)

window.mainloop()