
#if enemy is very close to the balloon when it explodes, (s)he is in the
#inner splash zone and gets wetter than someone who is further from
#the explosion in the outer splash zone.  The first two arguments specify the x- and y-coordinates of
#an object. The next two specify the x- and y-coordinates of the
#explosion. The final two specify the radii of the inner and outer splash
#zones. Based on the values given, determine whether the object falls
#inside of the inner splash zone, inside of the outer splash zone, or
#outside of both splash zones. You may find it useful to use the formula
#of a circle, centred at (p, q)

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
    
    