from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="Label", font=("Arial", 24, "bold"))
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

# def button_clicked():
#     my_label.config(text="Button got clicked")


def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_buttom = Button(text="Click me 2", command=button_clicked)
new_buttom.grid(column=2, row=0)
# button = Button(text="Click Me", command=button_clicked)
# button.pack()

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
