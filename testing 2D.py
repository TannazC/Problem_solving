# ============================================================================
# 1D Battleship
# Tannaz Chowdhury 
# Open in system shell > python "2D Battleship.py"
# 
# Two players determine how to position a fleet of pirate ships on a
# one-dimensional sea (i.e. along a line) subject to some rules. Once
# positioned, the players alternate turns guessing the locations of the
# ships and firing cannons at those locations in an attempt to sink them.
# The game ends when one player has hit all sections of all of their
# opponent’s ships. This player wins.
# There are game mode options to play with the computer acting as
# the second player. Modes vary in difficulty, which is accessed from a menu.
# Created using V model testing
# =============================================================================

from rich import print
import random
import math

ocean_symbol="[deep_sky_blue1]~[/deep_sky_blue1] "
hit_symbol="[bold red]O[/bold red] "
sunk_symbol="[bold red dim]X[/bold red dim] "

# Decide on the board size, e.g., 10x10
board_size = 10

# Represent the game board using a 2D list
game_board = [['.' for _ in range(board_size)] for _ in range(board_size)]

# Define constants for ship positions, hits, and misses
HIT = 'X'
MISS = 'O'


#---------------------------------------------- FUNCTION
#Input Validation for an integer
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

#---------------------------------------------- FUNCTION

import random


 
