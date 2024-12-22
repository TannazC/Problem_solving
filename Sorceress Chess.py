#Tannaz Chowdhury / J. Garvin
#Sorceress - checking the moves of a chess piece that moves like both a Rook and a Knight

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

#-------------------------------------------------- Main program ^^


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
    
    
    
    
    
