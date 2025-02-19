"""
Seven/Eleven Dice Game  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This is a dice-based game where the player rolls two dice to accumulate points.  
The goal is to roll as many times as possible **without rolling a sum of seven or eleven**,  
which resets the score to zero. The player can roll up to **10 times** or choose to stop at any point  
to keep their earned points.  

How It Works:  
1. The player rolls two six-sided dice.  
2. If the **sum is seven or eleven**, the player loses all points and the game ends.  
3. Otherwise, the player earns points equal to the **larger of the two dice values**.  
4. The game continues for up to **10 rolls** or until the player chooses to stop.  
5. The final score is displayed at the end of the game.  

This program demonstrates **random number generation, conditional logic,  
user interaction, and iterative loops** in a fun and interactive way.  
"""

import random
points=0
for roll in range(10):
    z=input("Roll your dice?(yes/no): ")
    if z=="yes":
        x=random.randint(1,6)
        print(x)
        y=random.randint(1,6)
        print(y)
        sums=x+y
        print("The sum is ", sums)
        if sums==7 or sums==11:
            points=0
            print("You lost your points! game over.")
            break
        else:
            if x>y:
                points+=x
                print("You've got ", x , " points!", "Now you have a total of", points," points.")
            else:
                points+=y
                print("You've got ", y , " points!", "Now you have a total of", points," points.")
        if roll == 10:
            print("You made it to the end! congrats.")
    else:
        print("You have a total of ", points, " points")
        print("Thanks for playing!")
        break
        
    
