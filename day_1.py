# intro
# day 1: print the hello world using the print function
print("Hello World")

# practise printing
print("Day 1- Python print function")
print("The function is declared like this:")
print("print('what to print')")

# concatination of strings using +
print("Hello"+" "+"Angela")

# Fix the code challenge
print("Day 1- String Manupulation challenge")
print("String concatenation is done using '+' sign")
print('e.g. print("Hello"+"World")')
print("New lines can be created with a backslach and n.")

# input function-- input() get user input in console
# print function will print the hello and the user input
print("Hello"+" "+input("What is your name?"))

# length funcion-- gives the length of the string
print(len(input("What is your name?")))

# variables-- it is a container to store data
name = input(" What is your name?")
length = len(name)
print(length)

# swaping of two values
a = input("a :")
b = input("b :")
temp = 0
temp = a
a = b
b = temp

print("a : "+a)
print("b : "+b)

# day 1 challenge
# 1. Create a greeting for your program.
print("Welcome to Band Generator")

# 2. Ask the user for the city that they grew up in.
city = input("Which city did you grew up in? \n")

# 3. Ask the user for the name of a pet
petname = input("What is the name of your pet? \n")
# 4. Combine the name of their city and pet and show them their band name.

print("Your generated band name is " + city + " " + petname)
# 5. Make sure the input cursor shows on a new line
