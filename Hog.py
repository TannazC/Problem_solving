#This variant is the same as Pig except at the beginning of the game the players decide the maximum number of dice
#which can be rolled on a turn. (10 is a good number.) Then, on a player's turn, they are free to choose any number
#of dice to roll up to the maximum allowed. This number may change from turn to turn, and they player is allowed to
#roll the dice as many times as they like. The player scores points equal to the total values of all the dice rolled,
#however if any of the dice roll a 1 then the player's score is zero for the turn and their turn ends.

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

