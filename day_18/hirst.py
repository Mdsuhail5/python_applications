import random
import turtle

color_list = [(121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218),
              (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

t = turtle.Turtle()
s = turtle.Screen()


s.colormode(255)
t.penup()
t.hideturtle()
t.setposition(-300, -300)

for i in range(10):
    for j in range(10):
        color = random.choice(color_list)
        t.dot(20, color)
        t.forward(60)
    t.backward(600)
    t.left(90)
    t.forward(60)
    t.right(90)

s.exitonclick()
