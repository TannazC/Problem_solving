#2. Treasure Hunt: Create a 12 x 12 grid. On square (0, 0), mark the player. Randomly select three of
#the remaining 143 squares, and place a “treasure” on them. The player should be able to enter one
#of four commands (N, S, E or W) to move in a cardinal direction. Ensure that the player remains on
#the grid at all times. If the player lands on a square containing a treasure, the hunt ends. Display a
#message showing the total number of steps taken.

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
        

#3. Treasure Hunt (version 2): Modify your program above so that whenever the player is 2 squares
#away from a treasure (horizontally, vertically or diagonally), a message is displayed indicating that
#they are close to a treasure.