# password manager
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)


# save password


def save():

    website = web_entry.get()
    email = emus_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \n Email: {email}"
                                       f"\n Password {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open(r"day_30\data.json", "r") as data_file:
                    # json.dump(new_data, data_file, indent=4)

                    # to update the data in the json we need 3 steps that is read, update and dump
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(r"day_30\data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            except json.JSONDecodeError:
                data = new_data
            else:
                # updating old data
                data.update(new_data)
                with open(r"day_30\data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)
                emus_entry.delete(0, END)


def find_password():
    website = web_entry.get()
    try:
        with open(r"day_30\data.json", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="no data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day_29\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

emus_label = Label(text="Email/Username:")
emus_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1)
web_entry.focus()

emus_entry = Entry(width=56)
emus_entry.grid(row=2, column=1, columnspan=2)


password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()
