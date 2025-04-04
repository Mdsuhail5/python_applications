#### scope####

# local scope
import random
from art import day12
enemies = 1


def increase_enemies():
    enemies = 2
    print(enemies)


increase_enemies()
print(enemies)


# global scope
player_health = 10


def drink_portion():
    potion_strength = 2
    print(potion_strength)


drink_portion()
print(player_health)

# global constants
PI = 3.1416


def const():
    PI = 78
    print(PI)


const()

# Number Guessing Game
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check the difficulty


def set_diff():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# check the number

def compare(guess_no, comp_no, turns):
    if guess_no > comp_no:
        print("Too high.")
        return turns - 1
    elif guess_no < comp_no:
        print("Too low.")
        return turns - 1
    else:
        print(f"You guessed it! The answer was {comp_no}")

# randomly computer choose a number


def game():
    print(day12)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    comp_num = random.randint(1, 100)
    turns = set_diff()

    guess = 0
    while guess != comp_num:
        print(f'You have {turns} attempts remaining to guess the number...')
        guess = int(input("Make a guess: "))
        turns = compare(guess, comp_num, turns)

        if turns == 0:
            print("You are out of attempts. You lose.")
            return
        elif guess != comp_num:
            print("Guess again")


game()
