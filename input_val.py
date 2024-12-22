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