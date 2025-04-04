# layouts manager
# pack - shows the widget one after the other
# place - places the widget at cordinates defined   label.place(x=0, y=0)
# grid - places the widget to columns and rows

from tkinter import *

window = Tk()
window.title("Layout Examples")
window.minsize(width=200, height=200)
window.config(padx=100, pady=100)  # adding padding
# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
# label.place(x=0, y=0)
label.grid(row=1, column=1)

# button


def do_it():
    print("do_it")


button = Button(text="click me", command=do_it)
button.grid(row=2, column=2)

# new button


def you_did_it():
    print("you_did_it")


button2 = Button(text="click me", command=you_did_it)
button2.grid(row=1, column=3)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(row=3, column=4)

window.mainloop()
