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