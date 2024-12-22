#Swapping Algorithm ASSIGNMENT
#Tannaz Chowdhury / ICS4U4 / K.Li

#Write a program to accept 3 numbers/letters/words  from a user  e.g number1, number2, number3
#then swap their positions. i.e the first number goes into 3rd position , the 3rd number moves
#to 2nd position and the second number moves into 3rd position. (randomized in each iteration)

import random
import math

#=================================================================================== FUNCTIONs

#input validation for integers within set parameters, take into account blank input
def get_integer(low=-math.inf, high=math.inf, prompt="Enter an integer: "):
    while True:
        value = input(prompt)
        if value.isspace() or value=="":
            continue
        value=value.strip(" ")
        if value[0] == "-":
            sign = -1
            value = value[1:]
        else:
            sign = 1
        if value.isdigit() and sign*int(value) >= low and sign*int(value) <= high:
            break
        else:
            print(f"This value is not an integer between {low} and {high}.")
    return sign * int(value)

#function to take ANY character/number/word so that the input is not blank (eliminating all spaces)
def get_item(prompt="Enter item: "):
    while True:
        value = input(prompt)
        if value.isspace() or value=="":
            continue
        value=value.strip(" ")
        return value

#function to take only specified letters
def get_let(letters, prompt):
    choice = input(prompt)
    choice=choice.strip(" ")
    while ((choice not in letters) and (not choice.isalpha())) or (choice.isspace() or choice==""):
        choice = (input("Invalid input, try again: "))
    return choice
#===================================================================================== MAIN PROGRAM

while True:
    iterations=get_integer(low=3, high=math.inf, prompt="Enter the amount of items you'd like to swap (minimum 3):  ")

    #iterate for the amount of items, and add the item given by input to a list
    items=[]
    for num in range(1,iterations+1):
        print(f"\n#{num}")
        item=get_item(prompt="Enter item: ")
        while item in items:
            print("You cannot swap two of the same thing!")
            item=get_item(prompt="Enter another item: ")
        items.append(item)

    # print original order of items
    print(f"\nOriginal order: {items}")

    # Randomize the positions
    random.shuffle(items)

    # Print the randomized order
    print(f"\nRandomized order: {items}")

    while True:
        print("Would you like to swap positions again?")
        again=get_let("YNyn", " (Y/N) :")
        if again.upper()=="N":
            break
        random.shuffle(items)
        # Print the randomized order
        print(f"\n (NEW!) Randomized order: {items}")
    
    print("Would you like to run the program again?")
    again=get_let("YNyn", " (Y/N) :")
    if again.upper()=="N":
        break

print("Thank you for using my swapping algorithm!")

