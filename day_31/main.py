from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WORDS_TO_LEARN_FILE = "day_31/data/words_to_learn.csv"
FRENCH_WORDS_FILE = "day_31/data/french_words.csv"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

rand_word = {}
words_dict = {}

# Load word data
try:
    words = pandas.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    original_words = pandas.read_csv(FRENCH_WORDS_FILE)
    words_dict = original_words.to_dict(orient="records")
else:
    words_dict = words.to_dict(orient="records")


def word_access():
    global rand_word, change_card
    window.after_cancel(change_card)
    try:
        rand_word = random.choice(words_dict)
        french_word = rand_word['French']
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(translation_text, text=french_word, fill="black")
        canvas.itemconfig(current_image, image=front_img)
        change_card = window.after(3000, flip_card)
    except IndexError:
        canvas.itemconfig(language_text, text="Completed!", fill="black")
        canvas.itemconfig(translation_text,
                          text="No more words to learn", fill="black")
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")


def right_click():
    try:
        words_dict.remove(rand_word)
        data = pandas.DataFrame(words_dict)
        data.to_csv(WORDS_TO_LEARN_FILE, index=False)
        word_access()
    except ValueError:
        pass


def flip_card():
    english_word = rand_word['English']
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(translation_text, text=english_word, fill="white")
    canvas.itemconfig(current_image, image=back_img)


# Initialize timer
change_card = window.after(3000, flip_card)

# Create UI
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
back_img = PhotoImage(file="day_31/images/card_back.png")
front_img = PhotoImage(file="day_31/images/card_front.png")
current_image = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
translation_text = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create buttons
right_image = PhotoImage(file="day_31/images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, command=right_click)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="day_31/images/wrong.png")
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=word_access)
wrong_button.grid(column=0, row=1)

# Start the app
word_access()
window.mainloop()
