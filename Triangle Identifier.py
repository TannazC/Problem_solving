"""
Triangle Type Checker  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This program checks whether three given side lengths can form a valid triangle  
based on the Triangle Inequality Theorem. If the given sides satisfy the theorem,  
the program classifies the triangle into one of three types:  

1. Equilateral - All three sides are equal.  
2. Isosceles - Two sides are equal.  
3. Scalene - No sides are equal.  

How It Works:  
1. The user inputs three positive integer values representing the triangle's sides.  
2. The program checks if the sum of any two sides is greater than the third side.  
3. If valid, the program determines the triangle type.  
4. If invalid, the program notifies the user that the values do not form a triangle.  

This program demonstrates input validation, conditional logic, and mathematical  
properties of triangles.  
"""


import random
import math

def trangle_checker(x,y,z):
    
    if (x+y)>z and (x+z)>y and (z+y)>x:
        print("This triangle fulfills the Triangle Inequality Theorum.")

        if x==y and y==z:
            print("Classification: Equilateral")
        elif x!=y and y!=z and x!=z:
            print("Classification: Isoceles")
        else:
            print("Classification: Scalene")
        
    else:
        print("This triangle does NOT work because it does not fulfill the Triangle Inequality Theorem.")
x=int(input("Enter a positive number: "))
y=int(input("Enter a positive number: "))
z=int(input("Enter a positive number: "))

trangle_checker(x,y,z)
