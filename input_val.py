"""
Description:
This function get_integer() prompts the user for an integer input within a specified range while ensuring input validation. The function prevents invalid inputs such as non-numeric characters or numbers outside the given range.

How It Works:
    Accepts parameters:
        low: The minimum acceptable integer value (default: -∞).
        high: The maximum acceptable integer value (default: ∞).
    prompt: The message displayed to request user input.
    Strips extra spaces from input and handles negative numbers separately.
    Validates the input:
        Ensures the input consists only of digits (excluding leading - for negative numbers).
        Converts the value to an integer.
        Checks if it falls within the allowed range.
        Keeps asking for input until the user enters a valid integer.
"""

import math

def get_integer(low=-math.inf, high=math.inf, prompt="Enter an integer: "):
    
    while True:
        value = input(prompt)
        value=value.strip(" ")
        if value[0] == "-":
            sign = -1
            value = value[1:]
        else:
            sign = 1
        if value.isdigit() and sign*int(value) >= low and sign*int(value) <= high:
            break
    return sign * int(value)

value=get_integer(low=0, high=10, prompt="Enter an integer: ")
print(value)
