#Tannaz Chowdhury / ICS4U4 / 2023.07.06 / 704464
#In the country of Rahmania, the cost of mailing a letter is 40 sinas for letters up to 30 grams.
#Write a program that prompts the user for a mass and then gives the cost of mailing a letter having that mass.

#============================================================================== Input Validation Function
#Checks if the input fits the 'low' and 'high' criteria specified using the given prompt. Enters a loop if it does not.
#This function takes into account alphabet input, blank input, and all else that would not be an integer to prevent crashing.

import math
from rich import print
def get_integer(low=-math.inf, high=math.inf, prompt="Enter an integer: "):
    while True:
        value = input(prompt)
        if value.isspace() or value=="":
            continue
        value=value.strip(" ")
        if value[0] == "-":
            sign = -1
            value = value[1:]
        else:
            sign = 1
        if value.isdigit() and sign*int(value) >= low and sign*int(value) <= high:
            break
        else:
            print(f"[red]This value is not an integer between {low} and {high}.")
    return sign * int(value)
#====================================================================================== Main Program

#friendly output message with validation for mass integer
print("Welcome to Rahmania. The costs of mailing packages from our country depends on weight.")

while rerun=="Y":

    mass=get_integer(low=0, high=math.inf, prompt="Enter the mass of your package (in grams) for an estimated cost: ")

    #40 sinas for letters up to 30 grams.
    #Between 30 g and 50 g, it is 55 sinas.
    #Between 50 g and 100 g, it is 70 sinas.

    if mass<=30:
        cost=40
    elif mass>30 and mass<=50:
        cost=55
    elif mass>50 and mass<=100:
        cost=70

    #Over 100 g, it costs 70 sinas plus an additional 25 sinas for each additional 50 g (or part thereof).
    #For example, 101 grams would cost 70 + 25 = 95 sinas. 149 g would also cost 95 sinas, because both of
    #these packages only use the first 50 g over 100 g.

    else:
        factor=1
        while True:
            #Checks how many times the additional weight is below 50 to calculate the additional cost of Sinnas (25 for every 50 or below grams)
            if (mass-100)<=(50*factor):
                cost=(25*factor)+70
                break
            #if it is still overweight, check for 100, 150 etc. then add cost above
            else:
                factor+=1
                continue
            
    #Use an fstring to output cost in a user-friendly way
    print(f"Your cost will be {cost} Sinnas")
    
    rerun= (input(" Run the program again? (Y/N): ")).upper()

print("Thank you!")






