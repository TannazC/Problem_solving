# In this game for young children, players move along a trail by drawing cards. Each card
#contains either one or two coloured symbols, which indicate how many spaces to move. For
#example, if a player draws a card with a single red symbol on it, s/he moves directly to the next red
#square on the path. In the case of two symbols, the player moves to the first square of that colour,
#then proceeds to the next square of the same colour. The game ends when one player reaches the
#end of the path, which occurs when a player draws a card and there are no more squares of that
#colour to travel. The game requires no strategy, and is predetermined by the order in which the
#cards are drawn.

#Write a program that simulates two players playing CandyLand. Create a list containing 102
#elements. The first element is the starting position, and the last element is the end position. The
#remaining 100 elements should be coloured squares, in the order red, green, blue, yellow. When it is

#a player’s turn, generate a random colour and move the player to the next square of that colour. In
#some cases, that player may move two spaces instead of one. When one player reached the end of
#the path, announce the winner.
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
    
    
    
    