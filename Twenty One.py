#Twenty-One: Beginning with a value of one, two players alternate saying a number that is 1-3
#greater than the previously mentioned number. The player who is forced to say twenty-one loses.
#For example, a game may be 1, 4, 6, 9, 10, 13, 16, 17, 19, 20, 21.

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
                
    
    
    
    