# ============================================================================
# PROGRAM NAME
# ICS3UO / J. Garvin
# Tannaz Chowdhury
# python "Battleship with AI.py"
# 
# Two players determine how to position a fleet of pirate ships on a
# one-dimensional sea (i.e. along a line) subject to some rules. Once
# positioned, the players alternate turns guessing the locations of the
# ships and firing cannons at those locations in an attempt to sink them.
# The game ends when one player has hit all sections of all of their
# opponent’s ships. This player wins.
# Additionally, there are game mode options to play with the computer acting as
# the second player. Modes vary in difficulty, which is accessed from a menu.
# =============================================================================

from rich import print
import inval
import random

ocean_symbol="[deep_sky_blue1]~[/deep_sky_blue1]"
hit_symbol="[bold red]O[/bold red]"
sunk_symbol="[bold red dim]X[/bold red dim]"

#---------------------------------------------- FUNCTION
# Identifies ship properties through either it's name or symbol, used for identifying type of ship sunken, etc.
#'known' variable is not specified because situations with limited information may still require all characteristics of the boat.
def ship_properties(known):
    if known.lower()=="sloop" or known.upper()=="S" :
        variable="S"
        length=2
        name="sloop"
    elif known.lower()=="brigatine" or known.upper()=="B" :
        variable="B"
        length=3
        name="brigatine"
    elif known.lower()=="frigate" or known.upper()=="F" :
        variable="F"
        length=4
        name="frigate"
    elif known.lower()=="galleon" or known.upper()=="G" :
        variable="G"
        length=5
        name="galleon"
    return name, variable, length
#--------------------------------------------- FUNCTION
# Validates the location of boat placement when setting up the player's board. Conditions must be met for the
# location to pass as true, as outlined below
def validate_location(fname,fsea,flocation,ocean_symbol):
    
    # Identify properties 
    fname, variable, flength=ship_properties(fname)
    flength-=1
    
    # Since boats are placed from the leftmost chosen location, the length cannot exceed the board
    if (flocation+flength<=49):

        # The space that the boat takes up cannot be occupied by any other ship/overlap (check from the chosen location to the right)
        for part_of_boat in range(0,flength):
            if fsea[flocation+part_of_boat]!=ocean_symbol:
                # Issues with location given will only be printed if it is an inputted value by a user
                if ((choice== 2 or choice==3) and player ==1) or choice==1:
                    print("[red]This location overlaps with another ship.\n")
                return False
        
        # End values have their own 'if' statements to prevent crashing when searching for a value that does not exist in the list
        
        # The location may be right under 50, so it must have a blank space to the left of it
        if (flocation+flength==49 and fsea[flocation-1]==ocean_symbol):
            return True
        # The location may just touch the left end of the board, so it must have a blank space to the right of it
        elif  flocation==0 and fsea[flocation+flength+1]==ocean_symbol:
            return True
        # If the boat is around the center, there must be spaces between this boat and any other
        elif fsea[flocation+flength+1]==ocean_symbol and fsea[flocation-1]==ocean_symbol:
            return True
        else:
            if ((choice== 2 or choice==3) and player ==1) or choice==1:
                print("[red]There must be at least 1 space between this boat and any other.\n")
            return False

    else:
        if ((choice== 2 or choice==3) and player ==1) or choice==1:
            print("[red] This value exceeds the board.\n")
        return False
    

#---------------------------------------------- FUNCTION
# Puts a given ship on a given board from the left-most chosen location, including validation and prompting input
# takes a known value of the ship (name), the sea to place it on and the 'number_of_ships' of iterations (how many of the same boat to place)

# Function version with COMPUTER GENERATED random locations (no user input or any output)
def set_ship_computergen(name,sea,number_of_ships):
    name, variable, length= ship_properties(name)
    
    # for every number of ships required, loop to place it
    for boat in range(1,number_of_ships+1):
        
        # Randomize location, validate, and if it is not valid the loop will continue to pick random numbers
        location=random.randint(1,49)
        validation=validate_location(name,sea,location,ocean_symbol)
        
        while validation==False:
            location=random.randint(1,49)
           
            validation= validate_location(name,sea,location,ocean_symbol)
            if validation== True:
                break
        # Placing the boat with the valid location
        sea= sea[0:location] + [variable]*length + sea[location+length:]
    return sea

# Function version with USER INPUT and output
def set_ship(name,sea,number_of_ships):
    name, variable, length= ship_properties(name)
    
    # For every number of ships required, loop to place it
    for boat in range(1,number_of_ships+1):
        
        # Ask for a location, validate, and if it is not valid (type, location etc.) the loop will continue to ask for a valid input
        print(f"[underline yellow2]{name} #{boat}")
        location=int(inval.get_integer(low=1, high=49, prompt="Enter the location to place your ship from it's leftmost side: "))-1
        
        validation=validate_location(name,sea,location,ocean_symbol)
        
        while validation==False:
            location=int(inval.get_integer(low=1, high=49, prompt="Enter a new VALID location: "))-1
            
            validation= validate_location(name,sea,location,ocean_symbol)
            if validation== True:
                break
        
        
        #Output and place the sea with the valid location
        sea= sea[0:location] + [variable]*length + sea[location+length:]
        print("".join(sea))
    return sea

#----------------------------------------------- FUNCTION
# Identifies if a boat was hit, missed or sunk. Takes arguement(s) of the location aimed at, the sea aimed at and it's VISIBLE list,
# as well as the symbol used to represent a boat which was hit

def cannon(hit_location,sea,visible,hit_symbol):
    
    # If the location is blank
    if sea[hit_location]==ocean_symbol:
        return "miss"
    else:
        name, variable, length= ship_properties(str(sea[hit_location]))
        
        # "parts" refers to the sections of the boat identified. This is used to identify how many sections of the same boat
        # are present on the board in order to match it to the full length of the boat. ex. if all 3 parts of a brigatine
        # are identified, that boat is sunk. 
        
        parts=1
        
        # **Extra spaces added around the board to prevent crashing with end values (near 50 or near 0) 
        visible=[ocean_symbol]*5 + visible_sea + [ocean_symbol]*5
        
        # Add to 'parts' for every section of the boat identified to the left or right
        for elm in range(1,length):
            if visible[hit_location+elm+5]==hit_symbol:
                parts+=1
            if visible[hit_location-elm+5]==hit_symbol:
                parts+=1
        # If all parts of the boat are identified to the left and right (including the location chosen) are identified, the boat sunk
        if parts>=length:
            return "sunk"
        else:
            return "hit"
        
# --------------------------------------------------------------------------------
# Computer AI to identify which move to make next using boats that have already been hit. Takes arugement(s) of the player's sea, the character
# for the ocean, past guesses. 'target' variable refers to the first 'hit symbol' identified on the boat. This symbol is what the computer
# will base the next move on.

def computer_move(visible_sea,ocean_symbol,target,past_guess):
    
    # Add extra spaces to prevent crashing for boats on the ends (+5 added to 'checking' lines of  'if' or 'for' code to offset these extra spaces)
    visible=[ocean_symbol]*5+visible_sea+[ocean_symbol]*5
    
    # Identify the next open adjacent location to the hit symbol
    for x in range(1,6):
    
        # If it is to the right, the next move should correspond
        if visible[target+x+5]==ocean_symbol:
            hit_location=target+x
            # If this location has already been guessed, move to the next vacant location to the left
            if hit_location in past_guess or target>45:
                for y in range(1,5):
                    if visible[target-y+5]==ocean_symbol:
                        hit_location= target-y
                        return hit_location
            else:
                return hit_location
        
        # If it is to the left, the next move should correspond
        elif visible[target-x+5]==ocean_symbol:
            hit_location=target-x
            # If this location has already been guessed, move to the next vacant location to the right
            if hit_location in past_guess or target<5:
                for y in range(1,5):
                    if visible[target+y+5]==ocean_symbol:
                        hit_location= target+y
                        return hit_location
            else:
                return hit_location
       
                        
#==================================================================================================================================== MAIN PROGRAM
#________________________________________________________________________________ MENU
            
print("[aquamarine3 blink]Welcome to battleship!")

choice = 1
while choice != 5:
    print("[bold aquamarine3]Select a game-mode or quit:")
    print("[bold medium_turquoise]1. Two Player")
    print("[bold medium_turquoise]2. Computer - Easy")
    print("[bold medium_turquoise]3. Computer - Challenge")
    print("[bold medium_turquoise]4. Tutorial/Instructions")
    print("[bold deep_pink4]5. Quit \n")
    choice = int(inval.get_integer(low=1, high=4, prompt="Enter one of the game-modes above: "))
    print(" ")
#_______________________________________________________________________________ TUTORIAL
    
    practice_sea=[ocean_symbol]*50
    
    if choice == 4:
        print("[plum2]First, you will be prompted to set up your board, which is 50 paces long. \nDifferent types of ships will have varying lengths:")
        print("[yellow2]Sloop[/yellow2] -> [plum2]2 units long[/plum2] \n[yellow2]Brigatine[/yellow2] ->[plum2] 3 units long[/plum2] \n[yellow2]Frigate[/yellow2] -> [plum2]4 units long[/plum2] \n[yellow2]Galleon[/yellow2] ->[plum2] 5 units long[/plum2] \n ") 
        print("[plum2]Ships will be placed from their left side of any of your chosen locations. \nTry placing a ship")
        print("[dim] Your practice board > [/dim]",("".join(practice_sea)),"\n ")
        practice_sea=set_ship("frigate",practice_sea,1)
        print("[orchid]**Remember when placing boats that there must be at least one space between one boat and any other")
        print(f"[plum2]To hit an opponent's boat, just enter any location when prompted to air your cannon. \nIf the location you hit turns into a {hit_symbol} symbol, you hit ONE PART of a boat.")
        print(f"[plum2]Aim around the {hit_symbol} to sink a ship, which will appear as a row of {sunk_symbol}")
        print("[orchid]Sink all 6 of your opponent's ships before they sink yours to win! \n")
#________________________________________________________________________________ TWO PLAYER OPTION

    if choice == 1:
                        
        sea1=[ocean_symbol]*50
        sea2=[ocean_symbol]*50

        player=1
        sea=sea1

        # Set ships---------------------------------------------------------
        for board in range(0,2):
            print(f"[bold bright_magenta]PLAYER {player}")
            
            #2 Sloops
            sea=set_ship("sloop",sea,2)
            print(" ")
            #2 Brigatine
            sea=set_ship("brigatine",sea,2)
            print(" ")
            #1 Frigate
            sea=set_ship("frigate",sea,1)
            print(" ")
            #1 Galleon
            sea=set_ship("galleon",sea,1)
            print(" ")
            
            
            if player==1:
                sea1=sea
                player=2
                sea=sea2
            else:
                player=1
                sea2=sea

        # Gameplay----------------------------------------------------------

        visible_sea1=[ocean_symbol]*50
        visible_sea2=[ocean_symbol]*50
        past_guesses1=[]
        past_guesses2=[]

        visible_sea=visible_sea2
        player=1
        opponent_sea=sea2
        past_guess=past_guesses1

        while True:
            
            # Introduce player and obtain location to hit on opponent's sea, checking if numbers fit within required parameters and weren't guessed before
            print(f"\n[bold bright_magenta]PLAYER {player}")
            print("[dim] Opponent board > ",("".join(visible_sea)))
            
            hit_location=int(inval.get_integer(low=1, high=50, prompt="Enter the location to aim your cannon: "))-1
            
            while hit_location in past_guess:
                print("[bold red]You guessed this location already!")
                hit_location=int(inval.get_integer(low=1, high=50, prompt="Enter the location to aim your cannon: "))-1
            past_guess.append(hit_location) # Add guesses to a list so they can be checked and won't repeat
            
            
            # If the chosen location is NOT blank, indicate that something has been hit and add hit symbol to sea
            if opponent_sea[hit_location]!=ocean_symbol:
                visible_sea= (visible_sea[0:hit_location])+[hit_symbol]+(visible_sea[hit_location+1:])
            
            # Use 'CANNON' function to determine if the action taken by the player results in just a hit, miss or sinking of a ship
            fate_of_boat= (cannon(hit_location,opponent_sea,visible_sea,hit_symbol))

            if fate_of_boat=="hit":
                print("[dark_red]You hit one of your opponent's boats!")
            
            elif fate_of_boat=="sunk":
                # Identify WHICH type of boat was sunk
                name,variable,length=ship_properties(opponent_sea[hit_location])
                print(f"[bold dark_red]You sunk a {name}!")
                
                # Replace all hit  symbols with a sunken boat symbol by determining the leftmost location of the boat
                # and appending sunken symbols equal length to the boat 
                for x in range(1,length+1):
                    
                    if hit_location-x<=0:
                        visible_sea= [sunk_symbol]*length + visible_sea[hit_location-x+1+length:]
                        break
                    elif opponent_sea[hit_location-x]==ocean_symbol:
                        visible_sea= visible_sea[0:hit_location-x+1] + [sunk_symbol]*length + visible_sea[hit_location-x+1+length:]
                        break
          
            else:
                print("[yellow2]You missed!")
            
            # The 'sea' is most efficiently altered as a list, but is nicely formatted as a string for printing
            # Print("".join(visible_sea))
            
            # Determine if the game is won by identifying if the sea contains sunken symbols equal to the TOTAL parts in each boat
            if (visible_sea).count(sunk_symbol)==19:
                break
            
            # Re-assign variables to switch for another round (other player), and 'return' the variables altered in the loop 
            if player==1:
                visible_sea2=visible_sea
                past_guesses1=past_guess
                sea2=opponent_sea
                
                player=2
                visible_sea=visible_sea1
                opponent_sea=sea1
                past_guess=past_guesses2
            else:
                visible_sea1=visible_sea
                player=1
                visible_sea=visible_sea2
                sea1=opponent_sea
                opponent_sea=sea2
                past_guesses2=past_guess
                past_guess=past_guesses1
                

        print(f"[bold bright_magenta]Player {player} [/bold bright_magenta] won this game!")
        
#________________________________________________________________________BOTH COMPUTER MODES
        
    elif choice == 2 or choice == 3: 
                        
        sea1=[ocean_symbol]*50
        sea2=[ocean_symbol]*50

        player=1
        sea=sea1

        # Set ships-----------------------------------------------------------
        
        # The player first sets their ships
        print(f"[bold bright_magenta]PLAYER {player}")
        print("".join(sea1))
        print(" ")
        
        #2 Sloops
        sea=set_ship("sloop",sea,2)
        print(" ")
        #2 Brigatine
        sea=set_ship("brigatine",sea,2)
        print(" ")
        #1 Frigate
        sea=set_ship("frigate",sea,1)
        print(" ")
        #1 Galleon
        sea=set_ship("galleon",sea,1)
        print(" ")
        
        sea1=sea
        player=2
        sea=sea2
            
        # The computer sets their ships after (randomized)
        #2 Sloops
        sea=set_ship_computergen("sloop",sea,2)
        #2 Brigatine
        sea=set_ship_computergen("brigatine",sea,2)
        #1 Frigate
        sea=set_ship_computergen("frigate",sea,1)
        #1 Galleon
        sea=set_ship_computergen("galleon",sea,1)
        
        player=1
        sea2=sea

        # Gameplay----------------------------------------------------------

        visible_sea1=[ocean_symbol]*50
        visible_sea2=[ocean_symbol]*50
        past_guesses1=[]
        past_guesses2=[]

        visible_sea=visible_sea2
        player=1
        opponent_sea=sea2
        past_guess=past_guesses1

        while True:
            
            if player == 1:
                # Introduce player and obtain location to hit on opponent's sea, checking if numbers fit within required parameters and weren't guessed before
                print(f"\n[bold bright_magenta]PLAYER {player}")
                print("[dim] Opponent board > ",("".join(visible_sea)))
                
                hit_location=int(inval.get_integer(low=1, high=50, prompt="Enter the location to aim your cannon: "))-1
                
                while hit_location in past_guess:
                    print("[bold red]You guessed this location already!")
                    hit_location=int(inval.get_integer(low=1, high=50, prompt="Enter the location to aim your cannon: "))-1
                past_guess.append(hit_location) # Add guesses to a list so they can be checked and won't repeat
                
                
                # If the chosen location is NOT blank, indicate that something has been hit
                if opponent_sea[hit_location]!=ocean_symbol:
                    visible_sea= (visible_sea[0:hit_location])+[hit_symbol]+(visible_sea[hit_location+1:])
                
                # Use the 'CANNON' function to determine if the action taken by the player results in a hit, miss or sinking of a ship
                fate_of_boat= (cannon(hit_location,opponent_sea,visible_sea,hit_symbol))

                if fate_of_boat=="hit":
                    print("[dark_red]You hit one of your opponent's boats!")
                
                elif fate_of_boat=="sunk":
                    # Identify WHICH type of boat was sunk
                    name,variable,length=ship_properties(opponent_sea[hit_location])
                    print(f"[bold dark_red]You sunk a {name}!")
                    
                    # Replace all hit  symbols with a sunken boat symbol by determining the leftmost location of the boat
                    # and appending sunken symbols equal length to the boat 
                    for x in range(1,length+1):
                        if opponent_sea[hit_location-x]==ocean_symbol:
                            visible_sea= visible_sea[0:hit_location-x+1] + [sunk_symbol]*length + visible_sea[hit_location-x+1+length:]
                            break
              
                else:
                    print("[yellow2]You missed!")
                
                # Determine if the game is won by identifying if the sea contains sunken symbols equal to the parts in each boat combined
                if (visible_sea).count(sunk_symbol)==19:
                    break
                
                # Re-assign variables to switch for another round, 'Returning' the ones altered in this loop
                visible_sea2=visible_sea
                past_guesses1=past_guess
                sea2=opponent_sea
                
                player=2
                visible_sea=visible_sea1
                opponent_sea=sea1
                past_guess=past_guesses2
                
#_________________________________________________________________ EASY (RANDOM) COMPUTER MODE
#REPEATED CODE - except there is NO input from the user
            elif player == 2: 
                if choice == 2: 
                
                    hit_location=random.randint(1,50)-1
                    
                    while hit_location in past_guess:
                        hit_location=random.randint(1,50)-1
                    past_guess.append(hit_location) # Add guesses to a list so they can be checked and won't repeat
                    
                    # If the chosen location is NOT blank, indicate that something has been hit
                    if opponent_sea[hit_location]!=ocean_symbol:
                        visible_sea= (visible_sea[0:hit_location])+[hit_symbol]+(visible_sea[hit_location+1:])
                    
                    # Use 'CANNON' function to determine if the action taken by the player results in a hit, miss or sinking of a ship
                    fate_of_boat= (cannon(hit_location,opponent_sea,visible_sea,hit_symbol))

                    if fate_of_boat=="hit":
                        print("Your boat was hit by [bold bright_magenta]player 2!")
                    
                    elif fate_of_boat=="sunk":
                        # Identify WHICH type of boat was sunk
                        name,variable,length=ship_properties(opponent_sea[hit_location])
                        print(f"[bold bright_magenta]Player 2[/bold bright_magenta] sunk a {name}!")
                        
                        # Replace all hit  symbols with a sunken boat symbol by determining the leftmost location of the boat
                        # and appending sunken symbols equal length to the boat 
                        for x in range(1,length+1):
                            if hit_location-x<=0:
                                visible_sea= [sunk_symbol]*length + visible_sea[hit_location-x+1+length:]
                                break
                            elif opponent_sea[hit_location-x]==ocean_symbol:
                                visible_sea= visible_sea[0:hit_location-x+1] + [sunk_symbol]*length + visible_sea[hit_location-x+1+length:]
                                break
                  
                    else:
                        print("Thankfully [bold bright_magenta]player 2[/bold bright_magenta] missed the shot.")
                    
                    # The 'sea' is most efficiently altered as a list, but is nicely formatted as a string for printing
                    print("[dim] Your board > ",("".join(visible_sea)))
                    
                    # Determine if the game is won by identifying if the sea contains sunken symbols equal to the parts in each boat combined
                    if (visible_sea).count(sunk_symbol)==19:
                        break
#________________________________________________________________ CHALLENGE (CALCULATED) COMPUTER MODE
                    
                if choice == 3: 

                
                    # If there is a hit symbol on the board, find the first one using index to identify the next move (target variable)
                    if hit_symbol in visible_sea:
                        target=visible_sea.index(hit_symbol)
                        hit_location=computer_move(visible_sea,ocean_symbol,target,past_guess)
                        
                    # If there is no hit symbol to identify the next move, randomly select a move
                    else:
                        hit_location=random.randint(1,50)-1
            
                    while hit_location in past_guess:
                        hit_location=random.randint(1,50)-1
                            
                    past_guess.append(hit_location) # Add guesses to a list so they can be checked and won't repeat
                    
                    # If the chosen location is NOT blank, indicate that something has been hit
                    if opponent_sea[int(hit_location)]!=ocean_symbol:
                        visible_sea= (visible_sea[0:hit_location])+[hit_symbol]+(visible_sea[hit_location+1:])
                    
                    # Use function to determine if the action taken by the player results in a hit, miss or sinking of a ship
                    fate_of_boat= (cannon(hit_location,opponent_sea,visible_sea,hit_symbol))

                    if fate_of_boat=="hit":
                        print("[dark_red]Your boat was hit by[/dark_red] [bold bright_magenta]player 2!")
                    
                    elif fate_of_boat=="sunk":
                        # Identify WHICH type of boat was sunk
                        name,variable,length=ship_properties(opponent_sea[hit_location])
                        print(f"[bold bright_magenta]Player 2[/bold bright_magenta] [dark_red]sunk a {name}!")
                        
                        # Replace all hit  symbols with a sunken boat symbol by determining the leftmost location of the boat
                        # and appending sunken symbols equal length to the boat 
                        for x in range(1,length+1):
                            if hit_location-x<=0:
                                visible_sea= [sunk_symbol]*length + visible_sea[hit_location-x+1+length:]
                                break
                            elif opponent_sea[hit_location-x]==ocean_symbol:
                                visible_sea= visible_sea[0:hit_location-x+1] + [sunk_symbol]*length + visible_sea[hit_location-x+1+length:]
                                break
                    else:
                        print("[yellow2]Thankfully[/yellow2] [bold bright_magenta]player 2[/bold bright_magenta][yellow2] missed the shot.")
                    
                    # The 'sea' is most efficiently altered as a list, but is nicely formatted as a string for printing
                    print("[dim]Your board > ",("".join(visible_sea)))
                    
                    # Determine if the game is won by identifying if the sea contains sunken symbols equal to the parts in each boat combined (LENGTHS MULTIPLIED BY BOATS)
                    if (visible_sea).count(sunk_symbol)==19:
                        break
                visible_sea1=visible_sea
                player=1
                visible_sea=visible_sea2
                sea1=opponent_sea
                opponent_sea=sea2
                past_guesses2=past_guess
                past_guess=past_guesses1
                
#____________________________________________________________ WIN MESSAGE AND RETURN TO TOP OF THE LOOP

        print(f"[bold bright_magenta]Player {player}[/bold bright_magenta] won this game!\n")
        print("".join(visible_sea)," \n")
        if choice==2 and player==2:
            print("[dim] How could you lose against the computer on easy mode.....?[/dim] [yellow2]Avenge yourself!\n")
        print("[blink reverse]Play again! \n") # Loop will return to menu for the user to either play again or quit
print("Thanks for playing! \n")
        