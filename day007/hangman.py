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
    #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] 
    #with 5 "_" representing each letter to guess.
    display = []
    for letter in chosen_word:
        display.append("_")

    print(display)
    #TODO-1-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    print(guess)

    #TODO-1-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #TODO-2-2 - If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].    
    i = 0
    for letter in chosen_word:
        if guess == letter:
            display[i] = letter
        i += 1
    
    print(display)