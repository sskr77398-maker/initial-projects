from words import words
import random
import string
import math

''' usually in hangamn game the player can try until he dies. in short.. he has infinite chance to select the correct sequence of 
letters for a valid word '''

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word  

def hangman():
    # Ensure "words" is imported correctly at the top of the file
    word = get_valid_word(words).upper()  # <-- ADD .upper() HERE
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 8

    # Getting user input only upper cases
    while (len(word_letters)) > 0 and lives > 0:
        # letters used
        # the join() method combines multiple strings into one string, placing a separator between them.

        print('you have' ,lives, 'lives left and you have already use these letters: ',' '.join(used_letters))
        # what current word is (e.i W_OD)
        word_list = [letter if letter in used_letters else '-' for letter in words]
        print('current word: ',' '.join(word_list))

        user_letter = input("guess the letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else :
                lives = lives - 1
                print("letter is not in word!")

        elif user_letter in used_letters:
            print("you have already used this letter. Please try again!!")

        else:
            print("invalid choice. Better luck next time")
            # gets here when word_letters [len] is 0 or when lives == 0.

    if lives == 0:
        print('you all chances are gone. sorry! the word is' , {word})
    else:
        print('you have guess correctly! the word is actually', {word})    


user_input = input("type randomly anything: ")
print(user_input)

hangman()
