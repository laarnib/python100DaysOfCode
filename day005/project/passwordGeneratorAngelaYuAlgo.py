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
#Much better way than my algorithm.
#Always learning
password_list = []
new_password = ""

#Add the random letters to list
for number in range(1, nr_letters + 1):
    password_list.append(letters[random.randint(0,len(letters)-1)])

#Add the random symbols to list
for number in range(1, nr_symbols + 1):
    password_list.append(symbols[random.randint(0, len(symbols)-1)])
    
#Add the random numbers to list
for number in range(1, nr_numbers + 1):
    password_list.append(numbers[random.randint(0, len(numbers)-1)])

#Randomly shuffle the order of the list
random.shuffle(password_list)

print(password_list)
#Add the characters of the shuffled password_list to the new_password string
for char in password_list:
    new_password += char

print(new_password)