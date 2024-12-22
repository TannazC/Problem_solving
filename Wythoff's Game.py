#Wythoff's Game:
#Plays a variant of Nim, with one heap of 21 objects.
# The player to remove the last object loses.
#if any heap runs empty, the player who takes it out loses

import random
print("You can either remove any number of objects from one heap, or any number from both. If ANY heap runs empty, the player who emptied it loses!")
HeapOne = random.randint(1,42)
HeapTwo = random.randint(1,42)
player = 1
choice=0
ObjectsRemoved1 = 0
ObjectsRemoved2 = 0
ObjectsRemovedBoth = 0

while HeapOne>0 and HeapTwo>0:
    print("player",player)
    choice=int(input("Choose a heap (1/2) or '3' for both: "))    
    
    while choice<=3 and choice>0:
        if choice==1 and HeapOne>0:
            ObjectsRemoved1 = int(input("Remove how many objects? "))
            HeapOne -= ObjectsRemoved1
        
        elif choice==2 and HeapTwo>0:
            ObjectsRemoved2 = int(input("Remove how many objects? "))
            HeapTwo -= ObjectsRemoved2
            
        
        elif choice==3 and HeapTwo>0 and HeapOne>0:
            ObjectsRemovedBoth = int(input("Remove how many objects from both? "))
            HeapTwo -= ObjectsRemovedBoth
            HeapOne -= ObjectsRemovedBoth
            
        if HeapOne<1 or HeapTwo<1:
            break
    
    if choice<=3 and choice>0:
        if player == 1:
            player = 2
        else:
            player = 1
    
    if HeapOne<1:
        if player==1:
            print("Heap one empty, player ",player,"won this round.")
        else:
            print("Heap one empty, player",player,"won this round.")
    if HeapTwo<1:
        if player==1:
            print("Heap two empty, player",player,"won this round.")
        else:
            print("Heap two empty, player",player,"won this round.")
    