#Read an arbitrary number of integers from the user and determine their average. Your program
#should not crash given invalid input, or given an inappropriate number of values to average

import inval
import math

n=inval.get_integer(low=1, high=math.inf, prompt="Enter the number of entries: ")
add=0
for entry in range(0,n):
    number=inval.get_integer(low=-math.inf, high=math.inf, prompt="Enter number: ")
    add+=number
    

average= add/n
print(average)