import constants

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_amount = 0

if size == "S":
    total_amount += constants.S_PIZZA
elif size == "M": 
    total_amount += constants.M_PIZZA
elif size == "L":
    total_amount += constants.L_PIZZA
else:
    total_amount += 0


if add_pepperoni == "Y":
    if size == "S":
        total_amount += constants.S_PIZZA_PEPPERONI
    else:
        total_amount += constants.ML_PIZZA_PEPPERONI
else:
    total_amount += 0


if extra_cheese == "Y":
    total_amount += constants.EXTRA_CHEESE
else:
    total_amount += 0


print(f"Your final bill is: ${total_amount}.")