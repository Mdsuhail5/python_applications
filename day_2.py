# Data types

# Strings
print("Hello"[1])
print("Hello"[4])
print("123"+"456")

# Integer
print(123)
print(123+456)

# Float
3.14159

# Boolean
True
False

# type function

num_char = str(len(input("What is your name? ")))
print(" your name has  "+num_char+" characters")

a = str(123)
print(type(a))

print(70+float("100.5"))

# add the digits of two digit number givens
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0])+int(two_digit_number[1]))

3+5
7-4
3*2
6/3
2**3

# PEMDAS
# ()
# **
# *
# /
# +
# -
print(3*3+3/3-3)

# BMI calculator
# bmi=weight(kg)/height**2(m**2)

weight = int(input("Enter your weight in kg :"))
height = float(input("Enter your height in m :"))

bmi = weight / height**2
bmi_int = int(bmi)

print("Your body mass index is :", bmi)
print("Your body mass index is :", bmi_int)

# round function
print(round(8/3))
print(round(2.666, 2))


print(8/3)
print(8//3)  # floor division rounds of to the integer value


# shorhand
score = 0
score += 1
height = 30
winning = True
# f-String
print(
    f"your score is {score}, your height is {height} and you are winning is {winning}")


# your life in weeks challenge
age = int(input("Enter your age :"))
days = 365*(90-age)
weeks = 52*(90-age)
months = 12*(90-age)
print(f"You have {days} days, {weeks} weeks, {months} months")

# tip calculator
print("Welcome to teip calculator.")

total_bill = float(input("What was your totalbill amount? "))
tip = float(input("What percentage tip would you like to give? 10,12, or 15? "))
split_no = int(input("How many people to split the bill? "))

each_split = (total_bill + (total_bill*tip/100))/split_no
print("Each person should pay :", round(each_split, 2))
