import random
import hangman_art
import hangman_words
#import hangman_words_kids

guessed_letters = []    #Will be used to check if user previously used the letter as a guess
stages_len = len(hangman_art.stages)

#Print hangman logo
print(hangman_art.logo)

#Check if word_list is empty and if it is exit game.
#Else, randomly choose a word from the word_list and assign it to a variable called chosen_word.
if not hangman_words.word_list:
    print("No words in list. Exiting Game...")
else:
    #chosen_word = random.choice(hangman_words_kids.word_list_kids)
    chosen_word = random.choice(hangman_words.word_list)
    player_lives_left = stages_len - 1   
    #print(chosen_word)   #for testing only

    #Create an empty List called display.
    #For each letter in the chosen_word, add a "_" to 'display'.
    display = []
    for letter in chosen_word:
        display.append("_")

    #Ask the user to guess a letter until user has guessed all the letters by checking number of "_"
    #and that player still has lives left.
    while display.count("_") > 0 and player_lives_left > 0:
        guess = input("\nGuess a letter: ")
        guess_length = len(guess)

        #Check if input is a letter. If it is, convert guess to lowercase
        #Else, let user that the input is not a letter and prompt user to guess again.
        if str.isalpha(guess) and guess_length == 1:
            guess = guess.lower()
        elif str.isalpha(guess) and guess_length > 1:
            print(f"Your {guess} is more than one letter. Please try again.")
            print(display)
            continue
        else:
            print(f"{guess} is not a letter. Please try again.")
            print(display)
            continue

        #Check if player previously used letter as a guess and if so, inform user and prompt user
        #to give another guess. Else, append the guess to guessed_letters list.
        if guessed_letters.count(guess) > 0:
            print(f"You already guessed the letter {guess}. Try again.")
            print(display)
            continue
        else:
            guessed_letters.append(guess)
        
            #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
            #If the letter at that position matches 'guess' then reveal that letter 
            #in the display at that position and change letter_match to True
            index = 0
            letter_match = False   

            for letter in chosen_word:
                if guess == letter and display[index] == "_":
                    display[index] = letter
                    letter_match = True
                index += 1
            
        
            #If letter the user guessed is not in the chosen word, let player know.
            if not letter_match:
                print(f"You guessed {guess}. That's not in the word. You lose a life.")
                player_lives_left -= 1

            #Print 'display' and you should see the guessed letter in the correct position
            #and every other letter replace with "_".
            print(display)

            #Print ASCII art that corresponds to the player's life
            #and the number of lives left
            print(hangman_art.stages[player_lives_left])
            
            if player_lives_left == 1:
                print(f"You only have {player_lives_left} life left.\nTake your time.  You can do this!")
            else:
                print(f"You have {player_lives_left} lives left.")


    if player_lives_left > 0:
        print(f"\n\nYou guessed {' '.join(display)}. That is correct!\n{hangman_art.balloon}Congratulations! You win!\n\n")
    else:
        print(f"\n\nI'm sorry you ran out of lives. Game over.\nThe word is {chosen_word}.")