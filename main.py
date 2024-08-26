from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_number_label.config(text=f"{km}")

# 1 entry, 4 labels, 1 button
miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

km_number_label = Label(text='0')
km_number_label.grid(column=1,row=1)

km_label = Label(text='Km')
km_label.grid(column=2,row=1)

calc_button = Button(text='Calculate',command=miles_to_km)
calc_button.grid(column=1, row=2)

window.mainloop()