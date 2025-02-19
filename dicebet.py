"""
Dice Betting Game - Two Player Challenge  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This is a **two-player dice betting game** where players bet on a number they believe  
they **won't roll** while rolling multiple dice. The objective is to **reach 50 points**  
without rolling the number they bet against.  

Game Rules:  
1. Each player chooses the number of dice they want to roll (between 1 and 9).  
2. Before rolling, they must bet on a number (1-6) they think they **won't roll**.  
3. They roll the dice:  
   - If they roll their bet number, they **BUST** and lose all their points.  
   - If they avoid their bet number, they **earn 2 points per die rolled**.  
4. The turn passes to the **next player** after each round.  
5. The first player to **reach 50 points wins**.  

How to Play:  
- Players alternate turns, following the betting and rolling process.  
- The game keeps track of **both players' points** and **displays the current score**.  
- If a player **busts**, their score resets to **0** and the other player takes over.  
- The game ends when **one player reaches 50 points**.  

This game integrates **randomization, loops, input validation, and turn-based mechanics**,  
making it an exciting **strategy and luck-based game**!  
"""


import random
Player=1
Bet=0
Points1=0
Points2=0
DiceRolled=1

#Assign number of dice to play with
NumberOfDice=int(input("Select any number of dice under 10: "))
while NumberOfDice>9 or NumberOfDice<0:
    NumberOfDice=int(input("Must be a posative integer under 10: "))


#Game loop
while Points1<50 and Points2<50:
    print("Player ", Player)
    
    #Bet dice number
    Bet=int(input("Choose a dice number between 1-6 that you do NOT think you'll role: "))
    while Bet>6 or Bet<0:
        Bet=int(input("Must be a posative integer under 6: "))
    
    #Roll dice
    print("You rolled :")
    for roll in range(NumberOfDice):
        DiceRolled=random.randint(1,7)
        print(DiceRolled) 
    #Bust or continue code + adding points
        if DiceRolled==Bet:
            print("^BUST, you lost all points")
            
            if Player==1:
                Points1=0
                break
            else:
                Points2=0
                break
        else:
            if Player==1:
                Points1+=(2)
            else:
                Points2+=(2)
         
        
    #Toggle player and display points
    if Player==1:
        print("(",Points1," points total to Player 1)")
        Player=2
    else:
        print("(",Points2," points total to Player 2)")
        Player=1
    
#winning and end game message
print("Player ",Player," won with 50 points!")
print("game end")
    
    
    
        

