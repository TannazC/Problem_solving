#Tannaz Chowdhury/704464/J. Garvin ICSemiPerimeter3U0/March 22
#Identifies whether randomly generated side lengths work to form a triangle, and classifies type, area and perimeter.
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