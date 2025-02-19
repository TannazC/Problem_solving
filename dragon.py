"""
Dragon Cave Adventure Game  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
A text-based adventure game where the player chooses between two caves,  
each containing a dragon. One dragon is friendly and shares treasure, while  
the other is hungry and eats the player. The outcome is randomized, adding  
an element of unpredictability to each playthrough.  

How to Play:  
1. The game introduces the player to the mystery of the two caves.  
2. The player selects Cave 1 or Cave 2.  
3. The game randomly determines if the chosen cave contains a friendly dragon  
   or a deadly dragon.  
4. The outcome is displayed with suspenseful delays for an immersive experience.  
5. The player can choose to play again after each round.  

This game is a great beginner project to practice conditional logic, loops,  
functions, and randomness in Python.  
"""


import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
         print('Gives you his treasure!')
    else:
         print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
