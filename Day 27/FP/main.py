from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)


# Row 0

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

# Row 1

equal_text = Label(text="is equal to")
equal_text.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

# Row 2


def button_click():
    km = int(miles_input.get()) * 1.6
    result.config(text=f"{km}")


button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()