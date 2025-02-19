"""
Coin Flip Simulation  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This program simulates flipping a **coin 1000 times** and tracks how many times it lands on heads.  
The user is asked to **predict the number of heads** before the simulation begins.  

How It Works:  
1. The user is prompted to make a guess and press enter to start.  
2. The program simulates **1000 coin flips**, counting the number of heads.  
3. Progress updates are displayed at:  
   - 100 flips  
   - 500 flips (halfway point)  
   - 900 flips  
4. The final count of heads is displayed at the end.  
5. The user is asked whether their guess was close.  

This program demonstrates basic probability concepts and is useful for understanding randomness and statistics.  
"""


import random
print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('900 flips and there have been ' + str(heads) + ' heads.')
    if flips == 100:
        print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
    if flips == 500:
        print('Halfway done, and heads has come up ' + str(heads) + ' times.')

print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
print('Were you close?')
