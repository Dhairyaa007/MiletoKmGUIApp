from tkinter import *

window = Tk()
window.title("Miles to KM Convertor")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def miles_km_convertor():
    miles_value = float(miles_input.get())
    km_value = miles_value * 1.609
    km_output.config(text=km_value)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=0)

km_output = Label(text=" ")
km_output.grid(column=1, row=1)
km_output.config(padx=10, pady=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=0)

calculate_btn = Button(text="Calculate", command=miles_km_convertor)
calculate_btn.grid(column=1, row=2)

window.mainloop()
