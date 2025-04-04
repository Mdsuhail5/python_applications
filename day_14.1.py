from art import high_low, vs
import random
import os
from game_data import data
print(high_low)
score = 0


def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, {account_desc}, {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        if guess == 'a':
            return True
        else:
            return False


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


account_b = random.choice(data)
game_continue = True
while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)

    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear_screen()
    print(high_low)
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
