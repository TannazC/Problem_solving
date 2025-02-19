"""
Dice Game: Race to 100  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This is a two-player dice game where players take turns rolling two six-sided dice  
to accumulate points. The goal is to reach exactly 100 points. Players can roll  
as many times as they like per turn but risk losing all points accumulated that turn  
if they roll a 1 on either die.  

How It Works:  
1. Players decide who goes first.  
2. On their turn, a player can:  
   - Roll two dice to accumulate points.  
   - Pass their turn to the other player.  
3. If a player rolls a **1 on either die**, their turn ends and they lose any points  
   gained that round.  
4. Play continues until one player reaches **100 points exactly** and wins the game.  

This program demonstrates turn-based logic, user decision-making, and probability-based  
risk assessment in an interactive game.  
"""


import random
points1=0
points2=0
player=1

while player!=1 or player!=2:
    player=int(input("Enter either player 1 or 2 to start : "))
    if player==1 or player==2:
        break
x=5
while x!=1 and points1<100 and points2<100:
    print("PLAYER ",player,":")
    y=input("Type 'y' to ROLL your dice or 'z' to SKIP your turn: ")
    
    if y=="z":
        if player == 1:
            player = 2
        else:
            player = 1
        continue
    
    if y=="y" or y=="Y":
        x=random.randint(1,6)
        p=random.randint(1,6)
        if player==1 and x!=1 and p!=1:
            points1+=x
            points1+=p
            print("First die rolled",x)
            print("Second die rolled",p)
            print(points1," points")
        elif player==2 and x!=1 and p!=1:
            points2+=x
            points2+=p
            print("First die rolled",x)
            print("Second die rolled",p)
            print(points2," points")
    
    if points1==100 or points2==100:
        break
    
    if y=="y" or y=="Y":
        if player == 1:
            player = 2
        else:
            player = 1

if points1==100 or points2==100:
    print("Player",player," wins with 100 points!")

if x==1:
    print("Player",player," loses because they rolled a 1.")



