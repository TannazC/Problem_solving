#Tannaz Chowdhury / ICS4U4 / K. Li / 2023
#BMI Calculator and classifier in Python (ver.3)

#The imperial BMI formula = Weight (LBS) x 703 ÷ Height (Inches²)
#The metric BMI formula = Weight (KG) ÷ Height (Metres²)

import math
from rich import print

#=============================================================================== Input validation function
#Checking if the float fits the 'low' and 'high' criteria, prompting another input if it doesn't (loop)
#Taking into account letter input, blank input
def get_float(low=-math.inf, high=math.inf, prompt="Enter a float: "):
    while True:
        value = input(prompt)
        if value.isspace():
            continue
        value=value.strip(" ")
        if value[0] == "-":
            sign = -1
            value = value[1:]
        else:
            sign = 1
        if (value.replace(".","").isdigit()) and sign*float(value) >= low and sign*float(value) <= high:
            break
        else:
            print("Try again")
    return sign * float(value)
#======================================================================================== Main program (menu)

choice=1
while choice!=3:
    print(f"\n1. Imperial BMI\n2. Metric BMI\n3. Quit")
    
    #GET choice of measurement
    choice=get_float(low=1, high=3, prompt="Enter the option for the measurement system in your region or quit: ")
    
    #If you quit, break the menu loop
    if choice==3:
        print("\nGood day sir!")
        break
        
    #Imperial calculations
    if choice==1:
        weight=get_float(low=0, high=math.inf, prompt="Enter your weight (Pound/LBS): ")
        height=get_float(low=0, high=math.inf, prompt="Enter your height (Inches/In): ")
        BMI  = (weight*703)/(height**2)
    
    #Metric calculations
    elif choice==2:
        weight=get_float(low=0, high=math.inf, prompt="Enter your weight (Kilogram/KG): ")
        height=get_float(low=0, high=math.inf, prompt="Enter your height (Meters/M): ")
        BMI  = (weight)/(height**2)
    
    BMI= round(BMI,1)
    
    #Classify catagory of BMI
    if BMI<=18.5:
        classification="Underweight"
    elif BMI>18.5 and BMI<=24.9:
        classification="at a Normal Weight"
    elif BMI>25 and BMI<=29.9:
        classification="Overweight"
    elif BMI>30 and BMI<=34.9:
        classification="Obese, class 1"
    elif BMI>35 and BMI<=39.9:
        classification="Obese, class 2"
    else:
        classification="Extremely obese"
    
    #Output message using fstring
    print(f"Your BMI is {BMI} , which means you are {classification}.")



        
        
