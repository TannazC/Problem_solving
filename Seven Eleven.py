#Seven/Eleven: A game is played where the player rolls two dice.
#If the sum of the dice is neither seven nor eleven, the player is awarded a number of points equal to the larger of the two values
#rolled. The player has up to 10 rolls to accumulate points; however, if the sum is either seven or
#eleven, the player loses all his/her points. The player can choose to stop at any point, keeping
#his/her points from previous rounds. Write a program that plays Seven/Eleven. Output the values of
#the rolls and the current score each round, and the final score (possibly zero) when the game ends.
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
        
    