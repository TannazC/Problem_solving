"""
Commencement Seating Arrangement Program  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This program helps organize and reorder staff seating arrangements for a  
Commencement ceremony. The user can enter a list of staff members and  
then interactively rearrange their seating order using specific commands.  

How It Works:  
1. The user enters staff names one by one to create an initial seating order.  
2. The user can then reorder staff using the following commands:  
   - "right of X" → Moves a staff member to the right of another.  
   - "left of X" → Moves a staff member to the left of another.  
   - "between X Y" → Moves a staff member between two others.  
3. The program continuously prompts for reordering until the user is satisfied.  
4. The final seating arrangement is displayed.  

This program integrates user input validation, list manipulation, and interactive seat reordering,  
providing an efficient way to organize seating for formal events.  
"""


import inval

row=[]

while True:
    name=str(inval.get_string(prompt="Enter a name, or 'X' to stop:  ",case="low"))
    if name!="X" and name!="x":
        row.append(str(name))
    else:
        break

def reorder(row,x,y,direction):
    posx=row.index(x)
    posy=row.index(y)
    if direction=="R" or direction=="r":
        del(row[posy])
        row.insert(posx+1,y)
        
    elif direction=="L" or direction=="l":
        del(row[posy])
        row.insert(posx-1,y)
    else:
        return false
    
    return row

while True:
    answer=input("Would you like to reorder? (Y/N): ")
    if answer!="y" and answer!="Y":
        break

    y=input("Who are you moving?: ")
    x=input("Who are you moving them around?: ")
    direction=input("In which direction? (L/R): ")

    newrow=reorder(row,x,y,direction)
    print(newrow)
    
