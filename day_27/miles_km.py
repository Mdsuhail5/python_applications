from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.config(padx=20, pady=20)  # adding padding

# entry
miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.get()
miles_input.grid(row=0, column=1)

# label * 4
miles_label = Label(text="Miles")
miles_label.config(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to ")
equal_label.config(text="is equal to ")
equal_label.grid(row=1, column=0)

km_result_label = Label(text="0")
km_result_label.config(text="0")
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.config(text="Km")
km_label.grid(row=1, column=2)

# Buttons


def calculate():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{km}")


# calls action() when pressed
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)


window.mainloop()
