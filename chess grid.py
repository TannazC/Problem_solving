"""
Chessboard Generator  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This program creates an **8x8 chessboard** with **standard chess piece placement**  
and allows the user to modify the board interactively. It includes:  
- **Row-based filling**: Users can select a row and a range to place multiple pieces.  
- **Single-slot filling**: Users can select specific board positions to place pieces.  
- **Pre-filled standard chess layout** with a loop-generated row of pawns.  
- **Live board updates** after every user action.  

How It Works:  
1. The program initializes a **standard chessboard setup**.  
2. Users can add, modify, or remove pieces by:  
   - Selecting a **row and range** to modify pieces.  
   - Selecting **specific coordinates** to modify a single square.  
3. The board updates dynamically after every modification.  
4. The user can **exit the modification phase** by entering `"x"`.  

This program provides **interactive chessboard editing** and teaches **2D list manipulation,  
user input validation, and grid-based placement**.
"""

import string

# Define Chess Pieces
PIECES = {
    "white": ["R", "N", "B", "Q", "K", "B", "N", "R"],
    "black": ["r", "n", "b", "q", "k", "b", "n", "r"]
}

# Create an 8x8 chessboard with default setup
def create_chessboard():
    board = [[". " for _ in range(8)] for _ in range(8)]

    # Place pieces
    board[0] = [piece + " " for piece in PIECES["black"]]  # Black major pieces
    board[1] = ["p " for _ in range(8)]  # Black pawns
    board[6] = ["P " for _ in range(8)]  # White pawns
    board[7] = [piece + " " for piece in PIECES["white"]]  # White major pieces

    return board

# Display the chessboard with labels
def draw_board(board):
    print("  A  B  C  D  E  F  G  H")  # Column labels
    for i, row in enumerate(board, start=1):
        print(i, "".join(row), i)  # Row labels
    print("  A  B  C  D  E  F  G  H")  # Column labels again

# Convert letter-based coordinates (e.g., "A1") to row and column indices
def parse_coordinates(coord):
    if len(coord) != 2:
        return None
    col, row = coord[0].upper(), coord[1]
    if col not in string.ascii_uppercase[:8] or not row.isdigit():
        return None
    return int(row) - 1, string.ascii_uppercase.index(col)

# Modify a range of positions in a row
def modify_row(board):
    while True:
        row_input = input("Enter the row number to modify (1-8) or 'x' to stop: ")
        if row_input.lower() == "x":
            break
        if not row_input.isdigit() or not (1 <= int(row_input) <= 8):
            print("Invalid row number. Try again.")
            continue

        row = int(row_input) - 1
        piece = input("Enter the piece to place (or '.' to clear): ")

        try:
            start_col, end_col = input("Enter start and end columns (e.g., A D): ").split()
            start_col, end_col = parse_coordinates(start_col + "1")[1], parse_coordinates(end_col + "1")[1]
        except (ValueError, TypeError):
            print("Invalid input. Try again.")
            continue

        if start_col > end_col:
            start_col, end_col = end_col, start_col

        for col in range(start_col, end_col + 1):
            board[row][col] = piece + " " if piece != "." else ". "

        draw_board(board)

# Modify a single position on the board
def modify_single_position(board):
    while True:
        coord = input("Enter coordinates to modify (e.g., B3) or 'x' to stop: ")
        if coord.lower() == "x":
            break

        parsed = parse_coordinates(coord)
        if not parsed:
            print("Invalid coordinates. Try again.")
            continue

        row, col = parsed
        piece = input("Enter the piece to place (or '.' to clear): ")
        board[row][col] = piece + " " if piece != "." else ". "

        draw_board(board)

# Main function
def main():
    board = create_chessboard()
    draw_board(board)

    while True:
        choice = input("Modify (R)ow, (S)ingle position, or (E)xit? ").lower()
        if choice == "r":
            modify_row(board)
        elif choice == "s":
            modify_single_position(board)
        elif choice == "e":
            break
        else:
            print("Invalid choice. Try again.")

    print("Final Chessboard:")
    draw_board(board)
    print("Program ended.")

if __name__ == "__main__":
    main()

 
