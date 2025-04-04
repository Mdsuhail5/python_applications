# def greet():
#     print("Welcome to functions!")
#     print("we will make cypher ceasor project.")


# greet()

# Area Calc

import math


def print_calc(height, width, cover):
    no_of_cans = math.ceil(height*width/cover)
    print(f"You'll need {no_of_cans} cans of paint.")


test_h = int(input("Height of the wall : "))
test_w = int(input("width of the wall: "))
coverage = 5
print_calc(height=test_h, width=test_w, cover=coverage)
