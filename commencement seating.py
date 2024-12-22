# Commencement Seating: Create a program that will help organize staff seated on stage during this
#year’s Commencement ceremony.

#In the first stage of your program, use a loop to input names of
#staff into a list, which represents a line of seats.

#In the second stage, use a loop to allow the user to
#reorder the staff until s/he is satisfied with the arrangement.

#To keep things user-friendly, your
#program should ask the user to enter the name of the staff to move, then to use one of three
#commands to determine their placement: “between X Y”, “right of X”, or “left of X”, where X and Y
#are existing names in the list. You will need to use to string methods to help parse user input.

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
    