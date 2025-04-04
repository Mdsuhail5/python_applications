from turtle import Turtle, Screen
import pandas as pd
image = r"day_25\us_states_game.py\blank_states_img.gif"
path = r"day_25\us_states_game.py\50_states.csv"

data = pd.read_csv(path)
screen = Screen()
t = Turtle()


screen.title("U.S.States Game")
screen.addshape(image)
t.shape(image)

list_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)} States Correct", prompt="What's another states name?").title()

    if answer_state == "Exit":
        missing_states = [
            state for state in list_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in list_states:
        guessed_states.append(answer_state)
        tn = Turtle()
        tn.hideturtle()
        tn.penup()
        state_data = data[data.state == answer_state]
        tn.goto(int(state_data.x), int(state_data.y))
        tn.write(answer_state)


screen.mainloop()
