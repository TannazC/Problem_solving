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
    