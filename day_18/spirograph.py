from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()

screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_circles(size_of_gap):
    for _ in range(int(365/size_of_gap)):
        tim.speed('fastest')
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+10)


draw_circles(10)
screen.exitonclick()
