from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colors = ['red', 'green', 'blue', 'yellow', 'black',
          'white', 'purple', 'pink', 'brown', 'grey']


def draw_shape(sides):
    angle = 360/sides
    tim.color(random.choice(colors))
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


draw_shape(3)
draw_shape(4)
draw_shape(5)
draw_shape(6)
draw_shape(7)
draw_shape(8)


screen.exitonclick()
