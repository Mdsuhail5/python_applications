# if else statement
# rollercoaster ride
print("Welcome to rollercoaster")
height = int(input("Enter your height :"))

if height >= 120:
    print("You can ride the rollercoaster! ")
    age = int(input("Enter your age :"))
    if age < 12:
        print(" Please pay 5$")
    elif age >= 18:
        print("Please pay 12$")
    else:
        print("Please pay 7$")
else:
    print("Sorry, you have to grow taller before you can ride.")


# odd or even number
number = int(input("Enter the number :"))
if number % 2 == 0:
    print(f"the number {number}  is even")
else:
    print(f"the number {number}  is odd")

# BMI calculator 2.o
height = float(input("Enter your height in m :"))
weight = float(input("Enter your weight in kg :"))

bmi = weight / (height*height)

print(f"your bmi is {bmi}")

if bmi < 18.5:
    print("You are underweight, and need to gain more muscles bud")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("overweight, need to shed some weight")
elif bmi < 35:
    print("obsese, need to shed a lot of weight dude")
else:
    print("clinically obese, consulte a doctor immedietly")

# leap year challenge
year = int(input("Enter the year :"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Pizza challenge
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L :")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")


if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25


if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is: ${bill}")

# Love Calculator
print("Welcome to the Love Calculator! ")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_strings = name1+name2
lower_string = combined_strings.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

true = t+r+u+e

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")

love = l+o+v+e

love_score = int(str(true)+str(love))
if (love_score < 10) or (love_score > 90):
    print(
        f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) or (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}.")
