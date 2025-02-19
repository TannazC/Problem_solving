"""
This program finds the closest multiple of 13 to a given positive integer (n > 0).

It ensures the input is a positive integer using a validation loop.
It calculates the largest multiple of 13 that is less than or equal to n (SmallMultiple).
It calculates the next multiple of 13 (LargeMultiple).
The program determines which of the two is closer to n and prints the result.
If n is equidistant between two multiples, the smaller multiple is chosen.
This function is useful in mathematical computations requiring alignment to nearest multiples for rounding or interval-based calculations.

"""
#PSUEDO CODE
#GET/INPUT posative integer n>0
#(validation loop)
#SET SmallMultiple to 13*(n//13)
#SET LargeMultiple to 13+SmallMultiple 
#IF difference of SmallMultiple<difference of LargeMultiple
#	OUTPUT SmallMultiple
#IF difference of SmallMultiple>difference of LargeMultiple
#	OUTPUT LargeMultiple
#ELSE
#	OUTPUT SmallMultiple


n=int(input("Enter a posative integer: "))
while n<0:
    n=int(input("Must be a posative integer: "))

SmallMultiple=(13*(n//13))
LargeMultiple=SmallMultiple+13

if (n-SmallMultiple)<(LargeMultiple-n):
    print("The multiple of 13 closest to ",n," is ",SmallMultiple)
elif (n-SmallMultiple)>(LargeMultiple-n):
    print("The multiple of 13 closest to ",n," is ",LargeMultiple)
else:
    print("The multiple of 13 closest to ",n," is ",SmallMultiple)
    
