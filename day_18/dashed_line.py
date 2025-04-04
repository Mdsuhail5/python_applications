from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
screen = Screen()
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


# or
# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color('white')
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color('black')

screen.exitonclick()
