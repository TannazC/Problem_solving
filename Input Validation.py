"""
User Input Validation Toolkit  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program provides a set of input validation functions to ensure  
users enter valid integers, floats, letters, or strings based on  
specified constraints. These functions help eliminate errors and  
improve user experience in interactive programs.  

Available Functions:  
1. **get_integer(low, high, prompt)**  
   - Ensures the user inputs a valid integer within a specified range.  

2. **get_float(low, high, prompt)**  
   - Ensures the user inputs a valid floating-point number within a range.  

3. **get_let(letters, prompt)**  
   - Ensures the user inputs a single valid letter from an allowed set.  

4. **get_string(prompt, case)**  
   - Ensures the user inputs a valid alphabetical string.  
   - Converts to uppercase or lowercase based on the `case` parameter.  

5. **get_single_string(prompt, case)**  
   - Ensures the user inputs a **single valid character**.  
   - Converts to uppercase or lowercase as needed.  

This program is useful for any application requiring structured input,  
helping prevent crashes and invalid entries by enforcing strict validation.  
"""


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

def get_let(letters, prompt):
    choice = input(prompt)
    choice=choice.strip(" ")
    while ((choice not in letters) and (not choice.isalpha())) or (value.isspace() or value==""):
        choice = (input("Invalid input, try again: "))
    return choice

def get_string(prompt="Enter a string: ",case="up"):
    choice = input(prompt)
    choice=choice.strip(" ")
    while not choice.isalpha() :
        choice = (input("Invalid input, try again: "))
    if case=="up" or case=="UP":
        choice=choice.upper()
    elif case=="low" or case=="LOW":
        choice=choice.lower()
    return choice

#get sentance

def get_single_string(prompt="Enter a string: ",case="up"):
    choice = input(prompt)
    choice=choice.strip(" ")
    while not choice.isalpha() or len(choice.strip(" "))!=1 :
        choice = (input("Invalid input, try again: "))
    if case=="up" or case=="UP":
        choice=choice.upper()
    elif case=="low" or case=="LOW":
        choice=choice.lower()
    return choice


