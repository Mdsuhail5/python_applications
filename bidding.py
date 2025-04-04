import os
from art import gavel
print(gavel)

bids = {}
bidding_finished = False


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bidding_record):
    highest = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    clear_screen()
    print(f"The winner is {winner} with a bid of ${highest}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid amount?: $"))
    bids[name] = price
    q = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if q == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif q == "yes":
        clear_screen()
