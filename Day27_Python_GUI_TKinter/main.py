#!/usr/bin/python3

from tkinter import *

window = Tk()
window.title("Mile to Kilometer converter")
window.config(padx=20, pady=20)


def converter():
    miles = float(mile_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km} km")


mile_input = Entry(width=14)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

km_result = Label(text=" 0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=converter)
calculate.grid(column=1, row=2)

window.mainloop()
