#For an arbitrary number of strings, determine how many are five-digit positive integers.

import random

n=random.randint(1,20)
numpos=0
word = "'"
for count in range(0,n):
    points=0
    numberofletters=random.randint(3,9)
    for letter in range(1,numberofletters):
        inletter=random.choice("ABCDEFGHIJKLMNOPXRSTUVWXYZ1234567890")
        word += inletter
    
    if word.isdigit() and len(word)==5:
        numpos+=1
    print(word)
    word = "'"
    
print(numpos," strings are five digit positive integer numbers. ")