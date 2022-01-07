import os
import time
import sys

#List of items for auction
items = {
    "camera": {
        "description": "Pentax  K1000 with a 50mm lens and cap.", 
        "start_bid": 40
    },
    "gameboy": {
        "description": "The original Nintendo Gameboy. It comes with Super Mario, Legend of Zelda, and Pokemon Red.", 
        "start_bid": 45
    },
    "wonderlamp": {
        "description": "Ever wanted to have your own genie? Well, here's your chance!\n\tRub the wonderlamp 150 times for Mr. Genie to appear.", 
        "start_bid": 150
    },
    "gramophone": {
        "description": "Need some vintage decoration in your home. Why not bring home this 1940 Gramophone", 
        "start_bid": 350
    },
    "bonsai": {
        "description": "The Chinese Elm Bonsai. It's a great starter tree for beginners.",
        "start_bid": 50
    }
}

#Bidders' data
bidders = {}

welcome_msg = "Welcome to the secret auction program"

#Prints an ASCII art saved in a txt file
#The value passed must match the name of the file where
#the are is saved.
def print_art(item):
    filename = item + ".txt"
    item_art = open(filename, 'r')
    print(''.join([line for line in item_art]))

def print_welcome_msg():
    print("\n\t", end="")
    for letter in welcome_msg:
        print(f"{letter} ", end="")
        sys.stdout.flush() 
        time.sleep(0.15)

#Clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_auction(item, description, start_price):
    #Auction keeps going until user says there are no more bidders.
    #Auction also stops if user enters a string other than 'yes' or 'no'.

    continue_auction = "yes"
    while continue_auction == "yes":
        clear_console()
        print("\n\n\n")
        print_art(item)
        print(f"\t{description}")
        print(f"\tThe starting bid price is ${start_price}")
        print("\n\n")
        bidder_name = input("\tWhat is your name? ")
        bid_amount = input("\tWhat is your bid? ")

        if not bid_amount:
           print("\tBid amount is not a valid number. Bidder ignored.")
           time.sleep(1)
           continue
        else:
            bid_amount = int(bid_amount)
            if not bidder_name:
                print("\tInvalid name. Bidder ignored.")
                time.sleep(1)
                continue
            elif bid_amount < start_price:
                print("\tBid price is less than starting bid price. Bidder ignored.")
                time.sleep(1)
                continue
            else:
                bid_amount = int(bid_amount)
                bidders[bidder_name] = bid_amount

        continue_auction = input("\tAre there any other bidders? Type 'yes' or 'no': ").lower()
        if continue_auction == 'yes':
            continue
        else:
            print(f"\tYou entered {continue_auction}. Ending the bid.")
    

def get_winner():
    winner = ""
    highest_bid = -1
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            winner = bidder
            highest_bid = bidders[winner]
    
    return winner



#Prints Welcome message and logo
clear_console()
print("\n\n\n")
print_art("logo")
print_welcome_msg()
print("\n\n")

print("\tThe first item is a...\n")
time.sleep(2)
for item in items:
    item_description = items[item]["description"]
    item_start_price = items[item]["start_bid"]
    start_auction(item, item_description, item_start_price)
    winner = get_winner()
    print(f"\n\tThe winning bid is {winner} with a bid of ${bidders[winner]}.")
    print("\tThe next item is...")
    time.sleep(2)

clear_console()
print("\n\n\tThat's all the items we have today.")
print("\tThank you for coming to the auction! Congratulations to all the winning bids!\n\n")