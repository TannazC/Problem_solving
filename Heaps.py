"""
Three-Heap Nim Variant  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This is a two-player variant of the classic game **Nim**, where players take turns  
removing objects from **three randomly sized heaps**. The first player to empty  
a heap **loses** the game.  

How It Works:  
1. The game starts with **three heaps** containing **random** objects (between 1 and 70).  
2. Players take turns selecting a heap and choosing how many objects to remove.  
3. If a player **empties a heap**, they **lose the game** immediately.  
4. The game continues until one heap reaches **zero objects**.  
5. The program announces the **losing player** and ends.  

This program demonstrates turn-based decision-making, input validation,  
and strategic gameplay in a competitive setting.  
"""


import random
HeapOne = random.randint(1,70)
HeapTwo = random.randint(1,70)
HeapThree = random.randint(1,70)
CurrentPlayer = 1
Choice=0
y=0
ObjectsRemoved = 0

#Begin game loop as long as no heap is empty
while HeapOne>0 or HeapTwo>0 or HeapThree>0:
    
    #Announce contents of each heap each round before descision making
    #For  checking bugs (would be removed for a game)
    print( "Heap One contains", HeapOne, "objects.")
    print("Heap Two contains", HeapTwo, "objects.")
    print("Heap Three contains", HeapThree, "objects.")
    
    #Choice of heap and validity
    print("Player",CurrentPlayer)
    Choice=int(input("Choose a heap: "))    
    while Choice<0 or Choice>3:
        Choice=int(input("Choose either heap 1, 2 or 3:  "))
    
    #Removing from chosen heap and validity
    ObjectsRemoved=int(input("Remove how many objects? (any number) "))
    while ObjectsRemoved<0:
        ObjectsRemoved=int(input("Must be a posative integer: "))
    
    if Choice==1 and HeapOne>0:
        HeapOne -= ObjectsRemoved
        
    elif Choice==2 and HeapTwo>0:
        HeapTwo -= ObjectsRemoved
        
    elif Choice==3 and HeapThree>0:
        HeapThree -= ObjectsRemoved 
    
    #Break and announce winner if any heap breaks
    if HeapOne<=0 or HeapTwo<=0 or HeapThree<=0:
        if HeapOne<=0:
            y=1
        elif HeapTwo<=0:
            y=2
        elif HeapThree<=0:
            y=3
        print("Heap",y," ran out!")
        break
    
    #Toggle player
    if CurrentPlayer == 1:
        CurrentPlayer = 2
    else:
        CurrentPlayer = 1

#Winning message
print("Player,",CurrentPlayer," loses!")
