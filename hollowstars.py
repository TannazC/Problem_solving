"""
Description:
This program generates a hollow rectangle using asterisks (*). The user specifies the width (n) and height (m), and the program prints a rectangular outline.

How It Works:
User Inputs

n: The width (number of * per row).
m: The height (number of rows).
Prints the First and Last Row

A full row of n asterisks (*) is printed at the top and bottom.
Prints the Hollow Rows (Middle Part)

The middle rows contain * at the start and end, with empty spaces in between.
The number of hollow rows is m - 2, ensuring at least a top and bottom row.
"""

n=int(input("length: "))
m=int(input("height: "))
starstr=n*"*"
print(starstr)
hollows=m-2
for number in range(0,hollows):
    space=int(n-2)
    hollowstr=str(("*")+(" "*space)+("*"))
    print(hollowstr)
print(starstr)
 
