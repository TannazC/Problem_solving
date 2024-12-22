#input val, loops, two players, random, goal
#two players roll any number of dice. They have to bet on what they WONT roll.
#If someone rolls something they bet on, they will 'bust' and lose all points, passing the baton to
#the other player
#each dice gives you 2 points if you DONT bust
#the goal is to gain more than 50 points without busting

import random
Player=1
Bet=0
Points1=0
Points2=0
DiceRolled=1

#Assign number of dice to play with
NumberOfDice=int(input("Select any number of dice under 10: "))
while NumberOfDice>9 or NumberOfDice<0:
    NumberOfDice=int(input("Must be a posative integer under 10: "))


#Game loop
while Points1<50 and Points2<50:
    print("Player ", Player)
    
    #Bet dice number
    Bet=int(input("Choose a dice number between 1-6 that you do NOT think you'll role: "))
    while Bet>6 or Bet<0:
        Bet=int(input("Must be a posative integer under 6: "))
    
    #Roll dice
    print("You rolled :")
    for roll in range(NumberOfDice):
        DiceRolled=random.randint(1,7)
        print(DiceRolled) 
    #Bust or continue code + adding points
        if DiceRolled==Bet:
            print("^BUST, you lost all points")
            
            if Player==1:
                Points1=0
                break
            else:
                Points2=0
                break
        else:
            if Player==1:
                Points1+=(2)
            else:
                Points2+=(2)
         
        
    #Toggle player and display points
    if Player==1:
        print("(",Points1," points total to Player 1)")
        Player=2
    else:
        print("(",Points2," points total to Player 2)")
        Player=1
    
#winning and end game message
print("Player ",Player," won with 50 points!")
print("game end")
    
    
    
        

