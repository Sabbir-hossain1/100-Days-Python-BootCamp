from tkinter import *

window = Tk()
window.title("Mile to Km Converter ")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)


def mile_to_km_cal():
    miles_value = mile_entry.get()
    km_value = round(float(miles_value) * 1.609)
    km_result_label.config(text=f"{km_value}")


equl_label = Label(text="is equal to ")
equl_label.grid(column=0, row=1)
equl_label.config(padx=5, pady=5)

mile_entry = Entry()
mile_entry.grid(column=1, row=0)
mile_entry.insert(END, string="0")
# mile_entry.config(padx=2, pady=2)

Miles_label = Label(text="Miles")
Miles_label.grid(column=2, row=0)
Miles_label.config(padx=5, pady=5)

# using entry

# km_entry = Entry()
# km_entry.grid(column=1, row=1)
# km_entry.insert(END, string="0")
# km_entry.config(padx=2, pady=2)

# using label

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)
km_result_label.config(padx=5, pady=5)


km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

cal_button = Button(text="Calculate", command=mile_to_km_cal)
cal_button.grid(column=1, row=2)
cal_button.config(padx=5, pady=5)

window.mainloop()
