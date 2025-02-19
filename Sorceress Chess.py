"""
Sorceress Chess Piece Move Validator  
Author: Tannaz Chowdhury  
Instructor: J. Garvin  
Date: 2023  

Description:  
This program checks the validity of a chess move for a custom piece called the **Sorceress**,  
which can move like both a **Rook** (horizontally or vertically) and a **Knight**  
(two squares in one direction and one in the other).  

How It Works:  
1. The user specifies the **board size** and the Sorceress's **current position**.  
2. The user inputs the **destination row and column** to check if the move is valid.  
3. The program verifies if:  
   - The move stays **within the board's boundaries**.  
   - The piece has **actually moved** (not remained in the same spot).  
   - The move follows **Rook movement rules** (straight lines).  
   - The move follows **Knight movement rules** (L-shaped moves).  
4. If the move is valid, the program prints **"your move is valid"**; otherwise, it states **"your move is invalid"**.  

This program demonstrates input validation, coordinate-based movement logic,  
and rule-based decision-making for chess-like games.  
"""


def positive_in(prompt):
    integer = int(input(prompt))
    while integer < 0:
        integer = int(input("Invalid value, try again: "))
    return integer

board_size= positive_in("Enter board size: ")
row= positive_in("Enter current row: ")
col= positive_in("Enter current column : ")
dest_row=positive_in("Enter destination row: ")
dest_col=positive_in("Enter destination column: ")

def valid_move(board_size,row,col,dest_row,dest_col):
    
    #check if move is different from starting position
    if dest_row==row and dest_col==col:
        print("You have not moved.")
        return False
    
    #check if move exceeds board
    if dest_row>board_size or dest_col>board_size:
        print("This exceeds the board, which has only,",board_size," squares.")
        return False
    
    #check if rook moves can be made (just horizontal OR just verticle)
    if dest_row==row and (dest_col>=col or dest_col<=col):
        return True
    elif dest_col==col and (dest_row>=row or dest_row<=row):
        return True
    
    #check if knight moves can be made (two horizontal + 1 vertical OR two vertical + 1 horizontal)
    if (dest_row==row+2 and dest_col==col+1) or (dest_row==row+2 and dest_col==col-1) or (dest_row==row-2 and dest_col==col+1) or (dest_row==row-2 and dest_col==col-1):
        return True
    elif (dest_col==col+2 and dest_row==row+1) or (dest_col==col+2 and dest_row==row-1) or (dest_col==col-2 and dest_row==row+1) or (dest_col==col-2 and dest_row==row-1):
        return True
    
    else:
        return False 
    
#-------------------------------------------------- Main program >>
    
if valid_move(board_size,row,col,dest_row,dest_col):
    print("your move is valid")
else:
    print("your move is invalid")
    
    
    
    
    
