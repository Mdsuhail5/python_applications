from turtle import Screen, Turtle
from paddle_create import Paddle
from ball import Ball
import time
import random
from scoreboard import Scoreboard

# Add power-up class


class PowerUp(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.shapesize(0.8, 0.8)
        self.penup()
        self.speed("fastest")
        self.active = False
        self.hideturtle()
        self.power_types = ["speed", "size", "slow"]
        self.current_power = ""

    def activate(self):
        if not self.active:
            self.active = True
            self.current_power = random.choice(self.power_types)
            self.showturtle()
            x = random.randint(-300, 300)
            y = random.randint(-200, 200)
            self.goto(x, y)

            # Set color based on power type
            if self.current_power == "speed":
                self.color("red")
            elif self.current_power == "size":
                self.color("green")
            elif self.current_power == "slow":
                self.color("blue")

    def deactivate(self):
        self.active = False
        self.hideturtle()


# Main game setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Enhanced Pong")
screen.tracer(0)

# Game objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
power_up = PowerUp()

# Game variables
difficulty_level = 1
power_up_timer = 0
power_up_active = False
power_up_effect_timer = 0
paused = False

# Function to toggle pause


def toggle_pause():
    global paused
    paused = not paused
    if paused:
        scoreboard.show_message("PAUSED")
    else:
        scoreboard.clear_message()

# Add the ability to restore original paddle sizes


def reset_paddle_sizes():
    r_paddle.shapesize(stretch_wid=5, stretch_len=1)
    l_paddle.shapesize(stretch_wid=5, stretch_len=1)


# Controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(toggle_pause, "space")

# Game loop
game_is_on = True
while game_is_on:
    if not paused:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Power-up logic
        power_up_timer += 1
        if power_up_timer > 200 and not power_up.active and random.random() < 0.01:
            power_up.activate()
            power_up_timer = 0

        # Check for power-up collision
        if power_up.active and ball.distance(power_up) < 15:
            if power_up.current_power == "speed":
                ball.move_speed *= 0.7  # Ball moves faster
                scoreboard.show_message("SPEED BOOST!", duration=2)
            elif power_up.current_power == "size":
                # Make the paddle that's about to receive the ball larger
                if ball.x_move > 0:
                    r_paddle.shapesize(stretch_wid=7, stretch_len=1)
                else:
                    l_paddle.shapesize(stretch_wid=7, stretch_len=1)
                scoreboard.show_message("PADDLE GROWTH!", duration=2)
                # Schedule paddle size reset after 10 seconds
                power_up_active = True
                power_up_effect_timer = 0
            elif power_up.current_power == "slow":
                ball.move_speed *= 1.5  # Ball moves slower
                scoreboard.show_message("SLOWDOWN!", duration=2)

            power_up.deactivate()

        # Handle power-up effect timers
        if power_up_active:
            power_up_effect_timer += 1
            if power_up_effect_timer > 100:  # About 10 seconds
                reset_paddle_sizes()
                power_up_active = False

        # Detect collision with top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddles - improved for angled bounces
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.xcor() < 350):
            # Calculate bounce angle based on where the ball hits the paddle
            relative_y = ball.ycor() - r_paddle.ycor()
            normalized_y = relative_y / 50  # Gives value between -1 and 1
            ball.y_move = normalized_y * 10  # Adjust vertical speed based on hit location
            ball.bounce_x()

        elif (ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.xcor() > -350):
            # Same angled bounce for left paddle
            relative_y = ball.ycor() - l_paddle.ycor()
            normalized_y = relative_y / 50
            ball.y_move = normalized_y * 10
            ball.bounce_x()

        # Detect when right paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()
            if scoreboard.l_score % 3 == 0:  # Increase difficulty every 3 points
                difficulty_level += 1
                ball.move_speed *= 0.9

        # Detect when left paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()
            if scoreboard.r_score % 3 == 0:
                difficulty_level += 1
                ball.move_speed *= 0.9

        # Check for game over
        if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
            game_is_on = False
            scoreboard.game_over()
    else:
        # Just update the screen while paused
        screen.update()
        time.sleep(0.1)

screen.exitonclick()
