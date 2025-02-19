"""
Swapping Algorithm  
Author: Tannaz Chowdhury  
Course: ICS4U4  
Date: 2023  

Description:  
This program accepts a list of **three or more numbers, letters, or words** from the user  
and swaps their positions randomly. The user can **reshuffle the order** as many times  
as they like before choosing to exit.  

How It Works:  
1. The user specifies the **number of items** they want to swap (minimum of 3).  
2. They enter each item, ensuring no duplicates.  
3. The program displays the **original order** of the items.  
4. The items are randomly shuffled and the **new order** is displayed.  
5. The user can choose to **reshuffle** as many times as they like.  
6. The program asks if the user wants to **restart with new items** or exit.  

Features:  
- Ensures input is **not blank** and removes extra spaces.  
- Prevents users from entering **duplicate items**.  
- Uses **random shuffling** for fair swaps.  
- Allows the user to reshuffle repeatedly before exiting.  

This program demonstrates **input validation, list manipulation, and randomization**  
while allowing users to interactively swap positions of items.  
"""

import random
import math

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

