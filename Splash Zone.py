
"""
Splash Zone Detection  
Author: Tannaz Chowdhury  
Github User: TannazC
Date: 2023  

Description:  
This program determines whether an enemy falls within the **inner** or **outer splash zone**  
of a water balloon explosion, or if they are outside both zones and remain dry.  
It calculates the distance between the enemy and the explosion center using  
the equation of a circle and compares it to the given radii.  

How It Works:  
1. The user inputs:  
   - `(x, y)`: Enemy's coordinates.  
   - `(p, q)`: Explosion center coordinates.  
   - `radiin`: Radius of the **inner splash zone**.  
   - `radiout`: Radius of the **outer splash zone**.  
2. The program calculates the squared distance between the enemy and the explosion center.  
3. It checks if the enemy is:  
   - Inside the **inner zone** (closer to the explosion).  
   - Inside the **outer zone** (farther but still affected).  
   - Outside both zones (completely safe).  

This program demonstrates coordinate-based distance calculations and conditional logic  
to classify objects based on their relative position to an explosion.  
"""


def SplashZone(x,y,p,q,radiin,radiout):

    #inner splash zone coordinate check
    if ((x-p)**2)+(( y-q)**2)<radiin**2:
        print("The enemy lies within the inner zone")
    
    #Outer splash zone coordinate check
    elif ((x-p)**2)+(( y-q)**2)<radiout**2:
        print("The enemy lies within the outer zone")
    
    else:
        print("The enemy does not lie within either zones and is unharmed.")

x=int(input("Enter value x : "))
y=int(input("Enter value y : "))
p=int(input("Enter value p : "))
q=int(input("Enter value q : "))
radiin=int(input("Enter value radius inner : "))
radiout=int(input("Enter value radius outer : "))

SplashZone(x,y,p,q,radiin,radiout)
    
    
