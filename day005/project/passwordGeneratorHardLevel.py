#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
character_list = [letters, symbols, numbers]
new_password = ""
total_charCount = nr_letters + nr_symbols + nr_numbers

while total_charCount > 0:
    char_list_index = random.randint(0, len(character_list) - 1)
    
    if char_list_index == 0 and nr_letters > 0:
        new_password += letters[random.randint(0, len(letters) - 1)]
        nr_letters -= 1
    elif char_list_index == 1 and nr_symbols > 0:
        new_password += symbols[random.randint(0, len(symbols) - 1)]
        nr_symbols -= 1
    elif char_list_index == 2 and nr_numbers > 0:
        new_password += numbers[random.randint(0, len(numbers) - 1)]
        nr_numbers -= 1
    else:
        continue
    total_charCount -= 1

print(new_password)