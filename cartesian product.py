#In mathematics, the Cartesian product is an operation that generates a new set from two given sets,
#X and Y. Specifically, the Cartesian product generates all ordered pairs, (x, y), where x is an
#element of X and y is an element of Y. For example, the Cartesian product of the sets X={1, 2} and
#Y={3, 4} consists of the pairs (1, 3), (1, 4), (2, 3) and (2, 4). Write a program that generates the
#Cartesian product of two tuples of arbitrary length, formatted as a set of ordered pairs.

cartesian_product = set()
X=(input("enter X coordinates seperated by '': "))
xX,yX=X.split()
X=(xX,yX)
Y=(input("enter Y coordinates seperated by '': "))
xY,yY=Y.split()
Y=(xY,yY)
for elm1 in X:
    for elm2 in Y:
        cartesian_product.add((elm1, elm2))
print(cartesian_product)
    


