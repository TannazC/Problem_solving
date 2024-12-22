import random
import inval
import math

def choose_word():
    catagory= inval.get_string(prompt="Enter the catagory: ",case="low")
    word= inval.get_string(prompt="Enter your secret word: ",case="low")
    while len(word)>6:
        word= inval.get_string(prompt="Word must have less than 6 characters : ",case="up")
    print("CATAGORY : ", catagory)
    return word

def display_word(word, guesses):
    display = ''
    for letter in word:
        if letter in guesses:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def play_game():
    word = choose_word()
    guesses = set()
    mistakes = 0
    while mistakes < 6:
        print("Word: " + display_word(word, guesses))
        print("Guesses remaining: " + str(6 - mistakes))
        print("Letters not guessed: " + ' '.join(sorted(set('abcdefghijklmnopqrstuvwxyz') - guesses)))
        
        letter = input("Guess a letter: ").lower()
        
        if letter in guesses:
            print("You already guessed that letter.")
       
        elif letter in word:
            guesses.add(letter)
            if set(word) == set(guesses):
                print("Congratulations! You guessed the word '" + word + "' correctly.")
                return
        else:
            mistakes += 1
    print("Sorry, you lost. The word was " + word)

play_game()