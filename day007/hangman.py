import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
if not word_list:
    print("No words in list. Exiting Game...")
else:
    chosen_word = random.choice(word_list)
    print(chosen_word)

    #TODO-2-1: - Create an empty List called display.
    #For each letter in the chosen_word, add a "_" to 'display'.
    display = []
    for letter in chosen_word:
        display.append("_")

    print(display)
    print(display.count("_"))
    #Ask the user to guess a letter until user has guessed all the letters by checking number of _s
    while display.count("_") > 0:
        guess = input("Guess a letter: ").lower()
        print(guess)
        
    #TODO-1-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #TODO-2-2 - If the letter at that position matches 'guess' then reveal that letter in the display at that position.  
        index = 0
        for letter in chosen_word:
            if guess == letter:
                display[index] = letter
            index += 1
    
        print(display)
    
    print(f"The word is {chosen_word}. You win!")