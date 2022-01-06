import os
import time

#List of items for auction
items = {
    "camera": "Pentax  K1000 with a 50mm lens and cap.", 
    "gameboy": "The original Nintendo Gameboy. It comes with Super Mario, Legend of Zelda, and Pokemon Red.", 
    "wonderlamp": "Ever wanted to have your own genie? Well, here's your chance!\nRub the wonderlamp 150 times for Mr. Genie to appear.", 
    "gramophone": "Need some vintage decoration in your home. Why not bring home this 1940 Gramophone", 
    "bonsai": "The Chinese Elm Bonsai. It's a great starter tree for beginners."
    }

#Bidders' data
bidders = {}


#Prints an ASCII art saved in a txt file
#The value passed must match the name of the file where
#the are is saved.
def print_art(item):
    filename = item + ".txt"
    item_art = open(filename, 'r')
    print(''.join([line for line in item_art]))

#Clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_auction():
    #Auction keeps going until user says there are no more bidders.
    #Auction also stops if user enters a string other than 'yes' or 'no'.
    while True:
        bidder_name = input("What is your name? ")
        bid_amount = int(input("What is your bid? "))

        bidders[bidder_name] = bid_amount

        continue_auction = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

        if continue_auction == 'yes':
            clear_console()
            continue;
        elif continue_auction == 'no':
            break;
        else:
            print(f"You entered an invalid response {continue_auction}. Ending auction...")


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
print_art("logo")
print("Welcome to the secret auction program.\n\n")

print("The first item is a...\n")
time.sleep(3)
for item in items:
    clear_console()
    print_art(item)
    print(f"\n{items[item]}")
    print("\n")
    start_auction()
    winner = get_winner()
    print(f"The winning bid is {winner} with a bid of ${bidders[winner]}.")
    time.sleep(3)

print("Thank you for coming to the auction! Congratulations to all the winning bids!")