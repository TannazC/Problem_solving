#Choose a player to go first. That player throws a die and scores as many points as the total shown on the die providing the die
#doesn’t roll a 1.The player may continue rolling and accumulating points (but risk rolling a 1) or end his turn.
#If the player rolls a 1 his turn is over, he loses all points he accumulated that turn, and he passes the die to next player.
#Play passes from player to player until a winner is determined.
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



