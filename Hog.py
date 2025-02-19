"""
Pig Dice Game - Variant with Custom Dice Rolls  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This is a two-player variant of the **Pig dice game** where players choose  
a maximum number of dice to roll per turn (up to 10). On their turn, players  
can roll **any number of dice** up to this limit, with the option to roll  
multiple times per turn. The objective is to **reach 100 points first**  
without rolling a **1**, which resets their points for the round.  

How It Works:  
1. Players choose a **maximum number of dice** they can roll per turn.  
2. On their turn, a player may:  
   - **Roll dice** (choosing how many within the set limit).  
   - **Stop rolling** to keep accumulated points.  
   - **Skip their turn** if they wish.  
3. If any die rolls a **1**, the player loses all points accumulated that round  
   and their turn ends immediately.  
4. Players take turns rolling until one **reaches 100 points** and wins.  
5. Players can also **stop the game early**, with the highest score determining  
   the winner.  

This program demonstrates user input validation, looping structures, turn-based  
decision-making, and probability-based risk assessment in an interactive game.  
"""

import random
points1=0
points2=0
player=1

t=int(input("Choose a posative (integer) number of dice to roll (max 10): "))
while t>10 or t<1:
    t=int(input("Number must be less than 10 and more than 1: "))

while player!=1 or player!=2:
    player=int(input("Enter either player 1 or 2 to start : "))
    if player==1 or player==2:
        break
x=5
Sum=0
while x!=1 and points1<100 and points2<100:
    print("PLAYER ",player,":")
    
    y=input("Type 'y' to ROLL your dice, 's' to stop or 'z' to SKIP your turn: ")
   
    while y not in ("ysz"):
        y=input("Must be a lowercase 'y','s' or 'z': ")
    
    if y=="z":
        if player == 1:
            player = 2
        else:
            player = 1
        continue
    if y=="y":
        for count in range(0,t):
            x=random.randint(1,6)
            if x!=1:
                print(x)
                Sum+=x
                x=0
            else:
                print("'1' was rolled!")
                print("Player",player," Lost!")
                break
        if player==1 and x!=1:
            points1+=Sum
            print("You have, ",points1," points")
        elif player==2 and x!=1:
            points2+=Sum
            print("You have, ",points2," points")
    if y=="s":
        break
    
    if points1==100 or points2==100:
        break
    
    if y=="y":
        if player == 1:
            player = 2
        else:
            player = 1

if points1==100 or points2==100:
    print("Player",player," wins with 100 points!")

if y=="s":
    print("Player one has : ",points1, " points.")
    print("Player two has : ",points2, " points.")
    if points1==points2:
        if points1==0:
            print("The game was not played long enough to accumulate points. Play again!")
        else:
            print("This is a tie!")
    elif points1>points2:
        print("Player one wins!")
    elif points1>points2:
        print("Player two wins!")

