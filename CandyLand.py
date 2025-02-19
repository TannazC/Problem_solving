"""
CandyLand Game Simulation  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program simulates a two-player game of **CandyLand**, where players move  
along a **predefined path of colored squares** based on the cards they draw.  
Each turn, a player draws a card that specifies a **color**, and they move to the  
next occurrence of that color in the path. The game continues until one player  
reaches the end of the path and is declared the winner.  

How It Works:  
1. The game board consists of **102 spaces**:  
   - The first space is "start".  
   - The last space is "end".  
   - The remaining 100 spaces cycle through **red, green, blue, and yellow**.  
2. Players take turns **drawing a card** (red, green, blue, or yellow).  
3. They **move to the next space of that color** in the path.  
4. The game continues until a player reaches the **end space**, winning the game.  
5. The program announces the winner and the final distance between the players.  

This program demonstrates **list manipulation, turn-based gameplay, and randomization**  
to simulate a board game experience in Python.  
"""


import random


path=["start"]+(["red", "green", "blue", "yellow"]*25)+["end"]

options=["red", "green", "blue", "yellow"]
player=1
pos1=0
pos2=0
while True:
    
    #toggle player
    print(f"Player {player}")
    
    #draw card
    card=random.choice(options)
    option=input("Enter Y to draw a card or N to quit: ")
    if option=="Y" or option=="y":   
        print(f"You drew {card}")
    else:
        break
    if path[pos1]=="end" or path[pos2]=="end":
        break
    
    #move and switch player
    if player==1:
        pos1= pos1 +(path[pos1:]).index(card)+1
        print(f"You are {pos1} spaces from the start.")
        player=2
    else:
        pos2= pos1+(path[pos2:]).index(card)+1
        print(f"You are {pos2} spaces from the start.")
        player=1
    
    
if pos1>pos2:
    print(f" Player 1 wins as they are {pos1-pos2} spaces ahead of player 2!")
    
else:
    print(f" Player 2 wins as they are {pos2-pos1} spaces ahead of player 1!")   
    
    
    
    
