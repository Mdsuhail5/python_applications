# procedural programming : where we setup procedures fuctions that do some particular thing and one procedure leads to another procedure and all in all and computer working from top to bottom and then jumping on the functions as needed
# object oriented programming: split a lot of task into smaller pieces and can be reused
# object oriented programming is trying to model real life objects which has attributes and methods , so basically object is combining data and function altogether same thing.
# each object has its own attributes i.e variable(has) and methods (does) i.e fuction
# it can have multiple objects
# multiple verisons of the same object from a blueprint i.e class and the individual object created from the class is call object
# data tied to object --> attributes
# function tied to object --> method
# constructing objects
# car=CarBlueprint()---> objec=class()
# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse1")
# timmy.shapesize(5)
# print(timmy)
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# object methods

from prettytable import PrettyTable

# Python Package Index
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
