#In this children’s game, two players alternate naming animals. The first player starts
#with any animal, such as elephant. The next player must name an animal that begins with the same
#letter as the one with which the previous animal ended. Thus, the second player could say tiger,
#then the first could say raccoon, and so on. When a player cannot name an animal, s/he loses. Write
#a program that lets two players plays the Animal Game. Use a list to store previous guesses, so that
#they cannot be reused. There should be some mechanism by which a player can indicate that s/he
#gives up, thus ending the game.

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
    
    