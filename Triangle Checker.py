
"""
Triangle Properties Calculator  
Author: Tannaz Chowdhury   
Course: ICS3U0  
Date: March 22, 2023

Description:  
This program generates three random side lengths and determines whether they  
can form a valid triangle based on the Triangle Inequality Theorem. If valid,  
the program classifies the triangle type, checks for right angles, and calculates  
the perimeter and area using Heron's Formula.  

How It Works:  
1. Generates three random side lengths between 1 and 10.  
2. Checks if the sides satisfy the Triangle Inequality Theorem.  
3. If valid, classifies the triangle as:  
   - Equilateral: All sides are equal.  
   - Isosceles: Two sides are equal.  
   - Scalene: No sides are equal.  
4. Determines if the triangle contains a right angle.  
5. Computes and displays the perimeter.  
6. Uses Heron's Formula to calculate and display the area (rounded to two decimal places).  
7. If the sides do not form a triangle, notifies the user.  

This program demonstrates conditional logic, mathematical computations,  
and the application of geometric principles in programming.  
"""


import random
import math
#side length one
x=random.randint(1,10)
#side length two
y=random.randint(1,10)
#side length three
z=random.randint(1,10)
print("Sidelengths generated: ", x,",",y,",",z)

#Check if it is a triangle
if (x+y)>z and (x+z)>y and (z+y)>x:
    print("This triangle fulfills the Triangle Inequality Theorum.")
    #Classify triangle
    if x==y and y==z:
        print("Classification: Equilateral")
    
    elif x!=y and y!=z and x!=z:
        print("Classification: Isoceles")
    
    else:
        print("Classification: Scalene")
    #Find if there is a right angle
    if ((x**2)+(y**2)==(z**2)) or  ((x**2)+(z**2)==(y**2)) or  ((z**2)+(y**2)==(x**2)):
        print("This triangle contains a right angle.")
    #Calculate perimeter
    Perimeter=x+y+z
    print("The Perimeter is : ",Perimeter," units.")
    #Calculate area (S=Semi Perimeter) using Heron's Formula
    S=(x+y+z)/2
    Area= math.sqrt(S*(S-x)*(S-y)*(S-z))
    RoundedArea=round(Area, 2)
    print("The Area is : ", Area," units, or ", RoundedArea, " units rounded.")
else:
    print("This triangle does NOT work because it does not fulfill the Triangle Inequality Theorem.")
