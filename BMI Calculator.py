"""
BMI Calculator and Classifier  
Author: Tannaz Chowdhury  
Course: ICS4U4  
Instructor: K. Li  
Date: 2023  

Description:  
This program calculates **Body Mass Index (BMI)** using both **Imperial**  
and **Metric** measurement systems. It also classifies BMI into standard  
weight categories based on medical guidelines.  

How It Works:  
1. The user selects a measurement system:  
   - **Imperial** (LBS & Inches) → Formula: (Weight × 703) ÷ (Height²).  
   - **Metric** (KG & Meters) → Formula: Weight ÷ (Height²).  
2. The program validates user input to ensure only **positive values** are accepted.  
3. The BMI is **calculated and rounded to one decimal place**.  
4. The BMI is classified into one of the following categories:  
   - Underweight (≤18.5)  
   - Normal Weight (18.6 – 24.9)  
   - Overweight (25 – 29.9)  
   - Obese (Class 1: 30 – 34.9, Class 2: 35 – 39.9, Class 3: 40+)  
5. The program outputs the **BMI value and classification**.  

This program demonstrates **user input validation, numerical calculations,  
conditional logic, and formatted output** for health-related computations.  
"""


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



        
        
