from turtle import Turtle, Screen
import random
import turtle as t
tim = t.Turtle()
screen = Screen()

screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
tim.speed('fastest')
tim.pensize(15)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen.exitonclick()
