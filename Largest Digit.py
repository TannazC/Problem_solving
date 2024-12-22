#Read a positive integer and determine the largest digit (e.g. for 17235 the largest digit is 7)

x=int(input("Enter a positive integer: "))
n=10
LargestNumber=0

while n<x:
    CurrentDigit=x//n
    if CurrentDigit>LargestNumber:
        LargestNumber=0
        LargestNumber+=CurrentDigit
    n*=10
print("The largest digit is : ", LargestNumber)
    
    