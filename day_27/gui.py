from tkinter import *
window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=250)

my_label = Label(text=" I am a Label", font=("Arial", 24, "italic"))
my_label.pack()
my_label['text'] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    print("I got Clicked")
    my_label.config(text="Button got clicked")
    data = input.get()
    my_label.config(text=data)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()


window.mainloop()
