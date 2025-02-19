"""
Hangman Word Guessing Game  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This is a **word guessing game** where one player selects a secret word (maximum  
6 characters) from a chosen category, and the other player attempts to guess  
the word one letter at a time. The game ends when the player correctly  
guesses the word or makes 6 incorrect guesses.  

How It Works:  
1. The first player **enters a category** and a **secret word** (must be 6 letters or fewer).  
2. The second player tries to guess the word by entering **one letter at a time**.  
3. If a guessed letter is **correct**, it is revealed in the word.  
4. If a guessed letter is **incorrect**, the player loses a life.  
5. The player has a maximum of **6 incorrect guesses** before losing.  
6. The game displays:  
   - The current progress of the word (e.g., `_ a _ _ _`)  
   - The number of **remaining guesses**  
   - The list of **unused letters**  
7. If the player correctly guesses the word, they win. Otherwise, the game  
   ends and the secret word is revealed.  

This program demonstrates **string manipulation, user input validation,  
set operations, and interactive gameplay mechanics** in Python.  
"""


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
