import random
import my_module

random.seed(121)
# to generate random integer numbe use random.randint
random_integer = random.randint(1, 10)
print(random_integer)

# modules are the files containing python code which can be class, function, variables etc
# modules act as libraries which can be imported that can utilize the code without needing to recreate it.
print(my_module.PI)


# to generate random float number the default value generation is between 0 to 1 and to generate till a certain number u need to multiply by it
random_float = random.random()*5
print(random_float)

# Heads or Tails challenge
test_seed = int(input("Create a seed number :"))
random.seed(test_seed)

number = random.randint(0, 1)
if number == 1:
    print("Heads")
else:
    print("Tails")

# list
l = ["apple", "mango", "kiwi"]
print(l)

# Who's paying
nameasCSV = input("Give me everybody's names, seperated by a comma :")
names = nameasCSV.split(",")
num_ppl = len(names)
paying_index = random.randint(0, num_ppl-1)
person_paying = names[paying_index]
print(f"person paying is {person_paying}")

# can be done using random for list using random.choice()
person_paying = random.choice(names)
print(f"person paying is {person_paying}")

# rock, paper, scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

choices = [rock, paper, scissors]
user = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

print(f"Your chose {choices[user]}")
print(f"Computer chose {choices[computer]}")
# rock<paper -->paper 0<1
# paper<scissors --> scissors 1<2
# scissors<rock --> rock 2<0
if user == computer:
    print("Its a draw")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You Win!")
else:
    print("Computer Wins")
