from tkinter import *

window =Tk()
window.title("Hello world~")
window.minsize(width=600, height= 400)


my_label = Label(text="Hello From Label!", font=("Arial", 25, "bold"))
my_label.pack(side="left")

#Config
# my_label["text"] = "New Text1213"
my_label.config(text="New Text4444")

#using function
def button_clicked():
    new_text = input.get() #Entry class
    my_label.config(text=new_text)

#Button
button = Button(text="Press me", command=button_clicked)
button.pack(side="left") #pack() to get it packed onto the screen, default position is top centered


#Entry
input = Entry(width=10)
input.place(x=300, y= 200) #custom location using x and y axis
window.mainloop()