from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def show_message(self, message, duration=None):
        """Display a temporary message on screen"""
        position = self.position()
        self.goto(0, 0)
        self.write(message, align=ALIGNMENT, font=("Courier", 24, "normal"))
        self.goto(position)

    def clear_message(self):
        """Clear temporary messages and redraw the scoreboard"""
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        winner = "LEFT" if self.l_score > self.r_score else "RIGHT"
        self.write(f"GAME OVER! {winner} WINS!",
                   align=ALIGNMENT, font=("Courier", 30, "normal"))
