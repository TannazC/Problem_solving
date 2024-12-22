#Tannaz Chowdhury / J. Garvin / 704464 / ICS3U / 2023-04-06
#a simple game in which a brave traveller makes their way through a series of tunnels populated by deadly monsters

import random
Distance=0
choice=0
MonsterTunnel=-1
print("Hello brave traveller. You are making your way through a series of tunnels, unknown to you which ones contain danger.")
print("Each tunnel you sucessfully get through will take you 100 meters forward. If you reach 1000 meters, you will successfully make it out of the mountain.")
print("Good luck!")

while True:
    
    #Choice of number of tunnels to choose from
    NumberOfTunnels=int(input("Choose the number of tunnels on your path (2-4): "))
    while NumberOfTunnels<2 or NumberOfTunnels>4:
        NumberOfTunnels=int(input("Must be a positive integer from 2-4: "))
    
    #Tunnel choice and validation
    MonsterTunnel=random.randint(1,NumberOfTunnels)
    choice=int(input("Now choose a tunnel number to enter: "))
    while choice<1 or choice>NumberOfTunnels:
        choice=int(input("You cannot escape any other way! Choose a tunnel number from 1-",NumberOfTunnels,": "))
    
    #No monster options
    if choice!=MonsterTunnel and Distance<1000:
        print("You evaded death! But wait... there are more ahead!")
        Distance+=100
    
    elif choice!=MonsterTunnel and Distance==1000:
        print("You see light ahead... you made it out of the tunnel!")
        print("You win!")
        break
    
    #Monster tunnel
    elif choice==MonsterTunnel:
        
        EscapeNumber=random.randint(1,10)
        print("You've encountered a monster! If you correctly guess the number of steps closest to the steps")
        EscapeChoice=int(input("you need to escape, you can sneak past it! (1-10): "))
        while EscapeChoice<1 or EscapeChoice>10:
            EscapeChoice=int(input("You must attempt to sneak past with a POSITIVE integer of steps BELOW 10: "))
        
        if EscapeChoice==EscapeNumber+1 or EscapeChoice==EscapeNumber-1 or EscapeChoice==EscapeNumber:
            print("You successfully snuck past the monster! But wait... there are more tunnels!")
            Distance+=100
            continue
        else:
            if MonsterTunnel==1:
                fate="were eaten by a giant spider!"
            if MonsterTunnel==2:
                fate="fell into a chasm!"
            if MonsterTunnel==3:
                fate="walked into a dragon's den!"
            if MonsterTunnel==4:
                fate="stepped on a bear trap!"
            print("You died! You ", fate )
            break
     

print("You travelled a total of ", Distance, " meters.")
print("Game over.")
    