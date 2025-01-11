from tkinter import *


def button_clicked():
    # my_label.config(text="Button got clicked")
    text = input.get()
    my_label.config(text=text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = Label(text="Label", font=("Arial", 20, "bold"))
#my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

# button
button = Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.get()
input.grid(column=3, row=2)


mainloop()
