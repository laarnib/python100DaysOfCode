import random
#Step 1 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
guessed_letters = []
stages_len = len(stages)

#TODO-1-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
if not word_list:
    print("No words in list. Exiting Game...")
else:
    chosen_word = random.choice(word_list)
    player_lives_left = stages_len - 1
    print(chosen_word)
    print(f"player lives left: {player_lives_left}")

    #TODO-2-1: - Create an empty List called display.
    #For each letter in the chosen_word, add a "_" to 'display'.
    display = []
    for letter in chosen_word:
        display.append("_")

    print(display)
    print(display.count("_"))
    #Ask the user to guess a letter until user has guessed all the letters by checking number of _s
    while display.count("_") > 0 and player_lives_left > 0:
        guess = input("Guess a letter: ").lower()
        print(guess)
        if guessed_letters.count(guess) > 0:
            print("You already guessed that letter.")
            continue
        else:
            guessed_letters.append(guess)
            print(guessed_letters)
        
            #TODO-1-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
            #TODO-2-2 - If the letter at that position matches 'guess' then reveal that letter in the display at that position.  
            index = 0
            letter_match = False

            for letter in chosen_word:
                if guess == letter and display[index] == "_":
                    display[index] = letter
                    letter_match = True
                index += 1
            
        
            if not letter_match:
                print("inside else")
                print(stages[player_lives_left - 1])
                player_lives_left -= 1
                print(f"player lives left: {player_lives_left}")

            print(display)
    
    if player_lives_left > 0:
        print(f"The word is {chosen_word}. You win!")
    else:
        print("You ran out of lives. Game over.")