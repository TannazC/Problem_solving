"""
Radical Simplification Tool  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program provides tools for working with square roots and radical expressions.  
It includes functions to check if a number is a perfect square, simplify radicals,  
and display them in proper mathematical notation.  

How It Works:  
1. **Check if a number is a perfect square**.  
2. **Simplify a given radical** into the form a√b, where a is the coefficient  
   and b remains under the square root.  
3. **Display the simplified radical** in a readable format using Unicode symbols.  

This program demonstrates mathematical logic, modular function design,  
and formatted output for representing radical expressions.  
"""


import math

#check if a number is square
def is_square_number(n):
    if math.sqrt(n)//1==0:
        return True
    else:
        return False

#radical to simple
def simplify_radical(r):

    if is_square_number(r):
        a = int(r ** 0.5)
        b = 1
    else:
        a = 1
        b = r
        for i in range(2, int(r ** 0.5) + 1):
            if r % (i ** 2) == 0:
                a *= i
                b = r // (i ** 2)
    return (a, b)

#simple to radical
def print_radical(a, b):
    if a == 1:
        print("\u221A", b)
        return
    else:
        print(f"{a}\u221A{b}")
        return

