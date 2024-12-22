# Plays a variant of Nim, with three heaps of any number of objects
# The first Player to empty a heap loses
# Heaps can contain a maximum of 70 objects 

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
