#1. Write a program that creates an 8 x 8 chessboard. Fill the board with pieces, according to the
#standard rules. Use any symbols you like. For the pawns on the second rank, use a loop to place
#them. Display the filled board. #fix

def blank_picture():
    pic = []
    for row in range(0,8):
        pic.append([". "]*8)
    return pic

def draw_picture(pic):
    for row in pic:
        chars = "".join(row)
        print(chars)

pic=blank_picture()
draw_picture(pic)

print("FILL IN YOUR ROWS")
while True:
    r = input("Enter the row to toggle: ")
    replace= input("enter character  or (x) to break:  ")
    if replace=="x" or replace=="X":
        break
    S, E = input("Enter start and end of section: ").split()
    r=(int(r))-1
    S=(int(S))-1
    E=(int(E))
    for elm in range(S,E):
        if pic[int(r)][int(elm)] == ". ":
            pic[int(r)][int(elm)]= replace + " "
    draw_picture(pic)

print("FILL IN SPECIFIC SLOTS")
while True:
    r, c = input("Enter the coordinates to toggle: ").split()
    replace= input("enter character  or (x) to break:  ")
    if replace=="x" or replace=="X":
        break
    r=(int(r))-1
    c=(int(c))-1
    if pic[int(r)][int(c)] == ". ":
        pic[int(r)][int(c)]= replace + " "
    draw_picture(pic)
    
#replace a section OR a row option / multiple points with the same piece  ----

 