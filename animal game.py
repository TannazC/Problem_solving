"""
Animal Naming Game  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This is a two-player word game where players take turns naming animals. Each new animal  
must start with the **same letter that the previous animal ended with**. If a player cannot  
think of an animal, they can enter 'w' to withdraw, and the other player wins.  

How It Works:  
1. Player 1 enters any animal to start the game.  
2. Player 2 must enter an animal that starts with the **last letter** of the previous animal.  
3. Players **cannot reuse animals**, so the program keeps a history of used words.  
4. If a player cannot name a valid animal, they enter 'w' to withdraw, ending the game.  
5. The program announces the **winner** based on who remains in the game.  

This game demonstrates **list management, input validation, and turn-based logic**,  
making it an engaging and interactive word-based challenge.  
"""

import inval 
player=1
print(f"Player {player}:")
animal=inval.get_string(prompt=" Enter an animal: ", case="low")
history=[]
history.append(animal)
player=2
while True:
    print(f"Player {player}:")
    print(f"beginning with the letter {animal[0]}")
    new_animal=inval.get_string(prompt=(" Enter an animal or 'w' to widthdraw: "), case="low")
    
    if new_animal=="w" or new_animal=="W":
        break
    
    while new_animal[0]!=animal[0]:
        new_animal=inval.get_string(prompt=(" Enter a valid animal name!: "), case="low")
        if new_animal in history:
            new_animal=inval.get_string(prompt=(" Enter an animal you havent used before: "), case="low")
    
    history.append(new_animal)
    animal=new_animal
    
    if player==1:
        player=2
    else:
        player=1

print(f"The winner is {player}")
    
    
