"""
Treasure Hunt - 12x12 Grid Game  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: [2023]  

Description:  
A simple text-based treasure hunt game where the player navigates a **12x12 grid**  
using "N", "S", "E", or "W" commands to find one of three randomly placed treasures.  
The game prevents movement off the grid and provides hints when near a treasure.  

How to Play:  
1. The player starts at (0,0) and moves using "N" (North), "S" (South), "E" (East), or "W" (West).  
2. Movement is restricted within the 12x12 grid.  
3. If the player reaches a **treasure square**, the game ends.  
4. If near a treasure, a hint ("The treasure is near...") is displayed.  
5. The game tracks and displays the total number of moves taken.  
"""


def blank_picture():
    pic = []
    for row in range(0,12):
        pic.append([". "]*12)
    return pic

def draw_picture(pic):
    for row in pic:
        chars = "".join(row)
        print(chars)

pic=blank_picture()

#starting pos
r=0
c=0
pic[r][c] = "I "

import random
r1=random.randint(2,12)
c1=random.randint(2,12)

r2=random.randint(2,12)
c2=random.randint(2,12)

r3=random.randint(2,12)
c3=random.randint(2,12)

print(f" the treasures are located at {r1},{c1} - {r2},{c2} - {r3},{c3}")

steps=0

while True:
    
    #input direction
    draw_picture(pic)
    direction=(input("choose a direction: ")).lower()
    
    #if move is valid, move   
    if (direction=="n") and r-1>0:
         pic[r][c] = ". "
         r-=1
         pic[r][c] = "I "
         steps+=1
    elif direction=="e" and c+1<12:
         pic[r][c] = ". "
         c+=1
         pic[r][c] = "I "
         steps+=1
    elif direction=="s" and r+1<12:
         pic[r][c] = ". "
         r+=1
         pic[r][c] = "I "
         steps+=1
    elif direction=="w" and c-1>0:
         pic[r][c] = ". "
         c-=1
         pic[r][c] = "I "
         steps+=1
    else:
        print("you cannot move that way.")
        continue
    
    #if you land on the treasure, break
    if (r==r1 and c==c1) or (r==r2 and c==c2) or (r==r3 and c==c3):
        break
    
    #if you are near the treasure, send a message
    if ((r>r1-2 and r<r1+1) and (c>c1-2 or c<c1+2)) or ((r>r2-2 and r<r2+2) and (c>c2-2 or c<c2+2)) or ((r>r3-2 and r<r3+2) and (c>c3-2 or c<c3+2)):
        print("the treasure is near...")
    
    
print("you found a treasure!")

pic[r][c]=="X "
        
