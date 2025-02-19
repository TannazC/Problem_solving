"""
Surface Area Calculator  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program calculates the total surface area of different shapes by allowing the user  
to add the areas of circles, rectangles, and triangles. The user can keep adding areas  
until they choose to display the total or quit the program.  

How It Works:  
1. The user selects an action from a menu:  
   - Add a circle (requires radius).  
   - Add a rectangle (requires length and width).  
   - Add a triangle (requires base and height).  
   - Display the total surface area.  
   - Quit the program.  
2. The program validates user input to ensure only positive values are accepted.  
3. The total surface area is updated with each shape added.  
4. The user can check the accumulated surface area at any time.  

This program demonstrates user input validation, function-based calculations,  
and iterative menu-driven interaction.  
"""


import math
def area_circle(radius):
    area = math.pi * radius**2
    return area
def area_rectangle(length, width):
    area = length * width
    return area
def area_triangle(base, height):
    area = base * height / 2
    return area
def get_integer(low=-math.inf, high=math.inf, prompt="Enter a value: "):
    integer = int(input(prompt))
    while integer < low or integer > high:
        integer = int(input("Invalid value, try again: "))
    return integer
def menu():
    print("What would you like to do: ")
    print("1. Add circle.")
    print("2. Add rectangle.")
    print("3. Add triangle.")
    print("4. Display total surface area.")
    print("0. Quit.")
    action = get_integer(low=0, high=4, prompt="Select an action: ")
    return action

# MAIN PROGRAM ================================================================

print("Welcome to the surface area calculator.")
action = menu()
surface_area = 0
while action != 0:
    if action == 1:
        radius = get_integer(low=0, prompt="Enter the radius: ")
        surface_area += area_circle(radius)
    elif action == 2:
        length = get_integer(low=0, prompt="Enter the length: ")
        width = get_integer(low=0, prompt="Enter the width: ")
        surface_area += area_rectangle(length, width)
    elif action == 3:
        base = get_integer(low=0, prompt="Enter the base: ")
        height = get_integer(low=0, prompt="Enter the height: ")
        surface_area += area_triangle(base, height)
    elif action == 4:
    print("The surface area is", round(surface_area, 2), "units^2.")
    action = menu()
print("Goodbye.")
