import os
from game_data import data
import random
from art import vs, high_low

print(high_low)
# Compare function to compare the answer


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def compare(opt1, opt2):
    if opt1['follower_count'] > opt2['follower_count']:
        return 'A'
    else:
        return 'B'

# Function to check the answer


def answer(user_answer, real_ans):
    if user_answer == real_ans:
        return True
    else:
        return False


score = 0
is_continue = True

while is_continue:
    game_on = True

    while game_on:
        A = random.choice(data)
        print(f"Compare A: {A['name']}, {A['description']}, {A['country']}.")
        print(vs)

        B = random.choice(data)
        while A == B:  # Ensure A and B are different
            B = random.choice(data)
        print(f"Against B: {B['name']}, {B['description']}, {B['country']}.")

        # Ask who has more followers, A or B
        user_answer = input(
            "Who has more followers? Type 'A' or 'B': ").upper()
        real_ans = compare(A, B)

        if answer(user_answer, real_ans):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Oops you are wrong! Final score: {score} ")
            game_on = False

    play_again = input(
        "Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    if play_again == 'y':
        is_continue = True
        score = 0
        clear_screen()
    else:
        is_continue = False
