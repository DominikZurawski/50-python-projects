import random
from hangman_words import word_list

import os
clear = lambda: os.system('cls')

again = 't'
while again == 't':
    own_word = input("Do you play with someone and want you input own word? input word or 'no/n' ").lower()
    if own_word == "no" or own_word == "n":
        chosen_word = random.choice(word_list)
    else: 
        chosen_word = own_word
    word_length = len(chosen_word)
    
    end_of_game = False
    lives = 6
    
    from hangman_art import logo
    print(logo)
    
    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"
    
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        clear()
    
        if guess in display:
            print(f"You've already guessed {guess}")
    
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
    
        #Check if user is wrong.
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
    
        print(f"{' '.join(display)}")
    
        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
    
        from hangman_art import stages
        print(stages[lives])
    
    again = input("Do you play again? y/n").lower()