from tkinter import *


def button_clicked():
    km = 1.609
    text = input.get()
    kms = km * float(text)
    output_label.config(text=int(kms))


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=100, pady=200)

# label
is_equal_label = Label(text="is equal to", font=("Arial", 20, "bold"))
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(column=2, row=1)

output_label = Label(text="", font=("Arial", 20, "bold"))
output_label.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

# Entry
input = Entry(width=7)
input.get()
input.grid(column=1, row=0)


window.mainloop()
