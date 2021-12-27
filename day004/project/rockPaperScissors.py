import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock, paper, scissors]

player_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print(computer_choice)

print(f"Player chose:\n{choices[player_choice]}\n\n")
print(f"Computer chose:\n{choices[computer_choice]}")

if player_choice == computer_choice:
   print("It's a draw.")
elif player_choice == 0 and computer_choice == 2:
  print("Congratulations! You win!")
elif player_choice == 1 and computer_choice == 0:
   print("Congratulations! You win!")
elif player_choice == 2 and computer_choice == 1:
  print("Congratulations! You win!")
else:
   print("You lose.")