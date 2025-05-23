import random
import os
from art import bj

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    print(bj)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    isgame_over = False
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    while not isgame_over:

        user_score = int(calculate_score(user_cards))
        computer_score = int(calculate_score(computer_cards))
        print(f"user cards { user_cards}and score {user_score}")
        print(f"comp cards { computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isgame_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                isgame_over = True

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack "
        elif user_score == 0:
            return "Win with a blackjack"
        elif user_score > 21:
            return "You went over. You lose"
        elif computer_score > 21:
            return "Opponent went over. You win"
        elif user_score > computer_score:
            return "You win"
        else:
            return "You lose"

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards} and your score is: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final socre {computer_score}")
    print(compare(user_score, computer_score))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


while input("Do you want to play a game? Type 'y' for yes and 'n' for no ") == 'y':
    clear_screen()
    play_game()
