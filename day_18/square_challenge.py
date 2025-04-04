import heroes
from turtle import *
timmy_the_turtle = Turtle()
screen = Screen()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


print(heroes.gen())
print(heroes.genarr(3))


screen.exitonclick()
