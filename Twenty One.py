"""
Twenty-One: Number Game  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This is a two-player game where players take turns choosing a number that is  
1 to 3 greater than the previously mentioned number. The game starts at 1,  
and the player forced to say 21 loses.  

How It Works:  
1. The game starts at 1, with Player 1 going first.  
2. Each player must pick a number that is 1, 2, or 3 greater than the last number.  
3. The game alternates turns until a player is forced to say 21, at which point they lose.  
4. The program validates input to ensure:  
   - The number is greater than the previous number by 1, 2, or 3.  
   - The number does not exceed 21.  

This program demonstrates turn-based logic, input validation, and game mechanics.  
It also introduces strategic decision-making, as players can try to trap their opponent.  
"""


pool=1
CurrentPlayer=1

while pool<21:
    
    #announce player
    print("Player: ",CurrentPlayer)
    
    #choice of number and adding to pool
    replaced=int(input("Enter a number that is 1-3 objects more than the previous: "))
    while ((replaced-pool)>3 or (replaced-pool)<1) or (replaced>21):
        replaced=int(input("Must be between 1 and 3 and cannot exceed the pool or be lower/equivelent: "))
    pool=replaced
    print("Pool :",pool)
    
    #breaking for 21
    if pool>=21:
        break
    
    #toggle player
    if CurrentPlayer==1:
        CurrentPlayer=2
    else:
        CurrentPlayer=1
        
print("Player ",CurrentPlayer, " loses!")
                
    
    
    
    
