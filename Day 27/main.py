import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")

window.mainloop()
