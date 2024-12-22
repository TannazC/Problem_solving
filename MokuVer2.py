import sys
sys.version

#Gomoku starter code
#You should complete every incomplete function,
#and add more functions and variables as needed.

#Note that incomplete functions have 'pass' as the first statement:
#pass is a Python keyword; it is a statement that does nothing.
#This is a placeholder that you should remove once you modify the function.

#Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023


def is_empty(board):  
    for row in board:
        for entry in row:
            if entry!=" ":
                return False
    return True 
    
# This function analyses the sequence of length length  that ends at location (y end, x end).
#The function returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence if semi-open, and "CLOSED"
#if the sequence is closed.
#Assume that the sequence is complete (i.e., you are not just given a subsequence) and valid, and
#contains stones of only one colour.

# open has nothing surrounding
# semi open has one side
# bounded is both sides

#The direction of a sequence can be represented by a pair of numbers (d_y, d_x) think: slope and rate of change
def is_bounded(board, y_end, x_end, length, d_y, d_x): 
    player = board[y_end][x_end]
    ls = None
    rs = None 

#-----------------------------
    if (d_y == 0 and d_x == 1) or (d_y == 1 and d_x == 0) :
        # left to right OR top to bottom 
        
        #check left side 
        if (x_end -(d_x*length)) == 0:
            ls = False
            #check bounded value at the edge of the board
        elif board[y_end -(d_y*length)][x_end -(d_x*length)]== " ": # if the leftmost spot is not empty
            ls = True
                    
        # check right side 
        if x_end == len(board[1])-1: #if at the end bounded
            rs = False
        elif board[y_end][x_end+1] == " ": #check one spot to the right of end
            rs = True

#------------------------------                   
    elif d_y == 1 and d_x == 1:
        #upper left to lower right -_
        
        #check left side at the end
        if ((x_end -(d_x*length)) == 0 or (y_end -(d_y*length)) == 0) or ((x_end -(d_x*length)) == 0 and (y_end -(d_y*length)) == 0):
            ls = False
            #check bounded value at the edge of the board
        elif board[y_end -(d_x*length)][x_end -(d_y*length)]== " ": # if the leftmost spot is not empty
            ls = True
        # check right side
        if (y_end == len(board[1]-1) or x_end == len(board[1]-1)) or (y_end == len(board[1]-1) and x_end == len(board[1]-1)): #if FIX
            rs = False
        elif board[y_end+1][x_end+1] == " ":
            rs = True
        else:
            rs = False
       
#---------------------------------             
    elif d_y == 1 and d_x == -1:
        # upper right to lower left _-
        
        #check left side 
        if ((x_end -(d_x*length)) == 0 or (y_end -(d_y*length)) == len(board[1])) or ((x_end -(d_x*length)) == 0 and (y_end -(d_y*length)) == len(board[1])):
            ls = False
            #check bounded value at the edge of the board
        elif board[y_end -(d_y*length)][x_end -(d_y*length)]== " ": # if the leftmost spot is not empty
            ls = True
        # check right side 
        if (y_end == 0 or x_end == len(board[1])) or (y_end == 0 and x_end == len(board[1])): 
            rs = False
        elif board[y_end-1][x_end+1] == " ":
            rs = True
        else:
            rs = False
#---------------------------------         
    if ls == True and rs == True:
        return "OPEN"
    elif ls == True or rs == True:
        return "SEMIOPEN"
    else:
        return "CLOSED"
    

#This function analyses the sequence (let’s call it R) of squares that starts at the location (y start,x start)
#and goes in the direction (d y,d x). a sequence of squares, which are adjacent either horizontally,
#or vertically, or diagonally. The function returns a tuple whose first element is the number of open
#sequences of colour col of length length in the row R, and whose second element is the number of
#semi-open sequences of colour col of length length in the sequence R.  

#Assume that (y start,x start) is located on the edge of the board. Only complete sequences count.
#For example, column 1 in Fig. 1 is considered to contain one open row of length 3, and no other rows.
#Assume length is an integer greater or equal to 2. --- identify all COMPLETE sequences of a colour (may not be a complete sequence)
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    #if i have length 4, it will detect length 3 semi closed twice!!
    #------------------------------ FIX EDGE CASES! IS BOUNDED IF SEQUENCE IS ON THE EDGE 
    #create a list of the "row" and then analyze
    # Create a list of the "row" from the given starting point and direction
    R = []
    open_seq_count, semi_open_seq_count = 0, 0
    board_size = len(board)

    # Construct the row R based on the direction given
    y, x = y_start, x_start
    while 0 <= y < board_size and 0 <= x < board_size:
        R.append(board[y][x])
        y += d_y
        x += d_x

    # Analyze the constructed row R
    i = 0
    while i < len(R):
        # Check if we have found a sequence of the target color
        if R[i] == col:
            # Check if this is the start of a sequence
            sequence_end = i
            while sequence_end < len(R) and R[sequence_end] == col:
                sequence_end += 1

            # Length of the detected sequence
            current_length = sequence_end - i

            if current_length == length:
                # Check left and right sides for open or semi-open
                left_open = (i == 0 or R[i - 1] == " ")
                right_open = (sequence_end == len(R) or R[sequence_end] == " ")

                if left_open and right_open:
                    open_seq_count += 1
                elif left_open or right_open:
                    semi_open_seq_count += 1

            # Move index to the end of the current sequence to continue searching
            i = sequence_end
        else:
            i += 1

    return open_seq_count, semi_open_seq_count
    

#This function analyses the board board. The function returns a tuple, whose first element is the
#number of open sequences of colour col of length lengthon the entire board, and whose second
#element is the number of semi-open sequences of colour col of length length on the entire board.
#Only complete sequences count. For example, Fig. 1 is considered to contain one open row of length
#3, and no other rows. 
#Assume length is an integer greater or equal to 2. 
def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    board_size = len(board)
    
    # Horizontal
    for y in range(board_size):
        y_start, x_start = y, 0
        d_y, d_x = 0, 1
        count1, count2 = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        open_seq_count += count1
        semi_open_seq_count += count2

    # Vertical
    for x in range(board_size):
        y_start, x_start = 0, x
        d_y, d_x = 1, 0
        count1, count2 = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        open_seq_count += count1
        semi_open_seq_count += count2

    # Diagonal with positive slope (/)
    for x in range(board_size):
        y_start, x_start = 0, x
        d_y, d_x = 1, -1
        count1, count2 = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        open_seq_count += count1
        semi_open_seq_count += count2

    for y in range(1, board_size):  # Start from row 1 to avoid double-counting the main diagonal
        y_start, x_start = y, board_size - 1
        d_y, d_x = 1, -1
        count1, count2 = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        open_seq_count += count1
        semi_open_seq_count += count2

    # Diagonal with negative slope (\)
    for x in range(board_size):
        y_start, x_start = 0, x
        d_y, d_x = 1, 1
        count1, count2 = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        open_seq_count += count1
        semi_open_seq_count += count2

    for y in range(1, board_size):  # Start from row 1 to avoid double-counting the main diagonal
        y_start, x_start = y, 0
        d_y, d_x = 1, 1
        count1, count2 = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        open_seq_count += count1
        semi_open_seq_count += count2

    return open_seq_count, semi_open_seq_count

#This function uses the function score() (provided) to find the optimal move for black. It finds the
#location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes the score of
#the board as calculated by score(). The function returns a tuple (y, x) such that putting a black
#stone in coordinates (y, x) maximizes the potential score (if there are several such tuples, you can
#return any one of them). After the function returns, the contents of board must remain the same.
import copy
def search_max(board):

    board_size = len(board)
    best_move = None
    max_score = float('-inf')

    # Iterate over each cell on the board
    for i in range(board_size):
        for j in range(board_size):
            # If the cell is empty, evaluate the move
            if board[i][j] == " ":
                # Create a deep copy of the board to simulate the move
                fake_board = copy.deepcopy(board)
                fake_board[i][j] = "b"  # Place a black stone

                # Calculate the score after placing the stone
                current_score = score(fake_board)

                # Update the best move if the current score is higher
                if current_score > max_score:
                    max_score = current_score
                    best_move = (i, j)

    # Return the best move found
    return best_move

# This function determines the current status of the game, and returns one of
#["White won", "Black won", "Draw", "Continue playing"], depending on the current status
#on the board. The only situation where "Draw" is returned is when board is full.   
def is_win(board):
    # Check for a win for both colors
    for col in ["b", "w"]:
        if detect_rows(board, col, 5) != (0, 0):
            if col == "b":
                return "Black won"
            elif col == "w":
                return "White won"

    # Check if the board is full - if all rows and columns are filled with no empty spaces
    is_full = all(cell != " " for row in board for cell in row)
    if is_full:
        return "Draw"

    # If no one has won and there are empty spaces, continue playing
    return "Continue playing"

#-------------------------------------------------------------------------------------------------------------
#This function computers and returns the score
#for the position of the board. It assumes
#that black has just moved.
def score(board): #DO NOT TOUCH 
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


#This function prints out the Gomoku board
def print_board(board):#DO NOT TOUCH 
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):#DO NOT TOUCH 
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                

#Analyses the position of the board by computing the number
#of open and semi-open sequences of both colours
def analysis(board): #DO NOT TOUCH 
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
#This function allows the user to play against a computer on a board
#of size board_size x board_size. this function interacts with the Ai engine
#by calling searchMax()
def play_gomoku(board_size): #DO NOT TOUCH 
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
#this helper function adds the sequence of stones of colour col of length length
# to board, starting at location (y,x) and moving in the direction (d_y,d_x). this function
# facilitates the testing of the AI engine
def put_seq_on_board(board, y, x, d_y, d_x, length, col): #DO NOT TOUCH 
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

#------------------------------------------------------------------------
def test_is_empty(): #DO NOT TOUCH 
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded(): #DO NOT TOUCH 
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN': 
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row(): #DO NOT TOUCH 
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows(): #DO NOT TOUCH 
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max(): #DO NOT TOUCH 
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions(): #DO NOT TOUCH 
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests(): #DO NOT TOUCH 
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    play_gomoku(8)
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()
    easy_testset_for_main_functions()
    some_tests()
