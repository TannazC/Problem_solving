"""
Three-Digit Number Matching Game  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This game challenges the player to guess a **random three-digit number**.  
The player earns points for each matching digit in the **same position**  
as the randomly generated number.  

How It Works:  
1. The program generates a **random three-digit number** (100-999).  
2. The player inputs their own **three-digit guess**.  
3. The program compares the **first, middle, and last digits** of both numbers.  
4. The player earns **one point per matching digit** in the correct position.  
5. The program displays which digits match and the total score.  
6. If the player enters an invalid number (not in the 100-999 range),  
   they are prompted to try again.  

This program demonstrates input validation, number manipulation using  
integer division and modulus, and conditional logic for scoring.  
"""


import random
target = random.randint(100, 999)
print("I'm thinking of a three-digit number.")
print("Each digit that matches one of mine earns a point.")

while True:
    user_num = int(input("Enter a three-digit positive number: "))
    
    if user_num>=100 and user_num<=999:
        print("The number is ", target, ".", sep="")
        correct = 0
        if user_num % 10 == target % 10:
            print("The last digits match.")
            correct += 1
        if user_num // 10 == target // 10:
            print("The middle digits match.")
            correct += 1
        if user_num // 100 == target // 100:
            print("The first digits match.")
            correct += 1
        if correct == 0:
            print("Nothing matches.")
        print("You scored", correct, "points.")
        break
    else:
        print("Your Input is inavlid. Try again.")
