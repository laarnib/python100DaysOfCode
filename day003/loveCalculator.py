# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1 + name2

true_count = 0
love_count = 0
love_score = 0

# Check the number of times letters in TRUE occurs
for letter in combined_name.lower():
    if letter == "t" or letter == "r" or letter == "u" or letter == "e":
        true_count += 1

    if letter == "l" or letter == "o" or letter == "v" or letter == "e":
        love_count += 1


love_score = true_count * 10 + love_count

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


# Angela's way of counting the letter
# t = combined_name.lower().count("t")