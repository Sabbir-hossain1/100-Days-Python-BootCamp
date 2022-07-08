from tkinter import *


def button_clicked():
    label.config(text=entry.get())


window = Tk()
window.title("Mile to Km Converter ")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

label = Label(text="New Text", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button1 = Button(text="New Button", command=button_clicked)
button1.grid(column=2, row=0)
button1.config(padx=10, pady=10)

entry = Entry(width=10)
print(entry.get())
entry.grid(column=3, row=3)

window.mainloop()
