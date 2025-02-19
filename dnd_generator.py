"""
Dungeons & Dragons Character Stats Generator  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This program generates **randomized character attributes** for a Dungeons & Dragons game.  
It follows the standard method of rolling **four six-sided dice (d6)** and summing the  
three highest values to determine the six core attributes:  

- Strength  
- Constitution  
- Dexterity  
- Wisdom  
- Intelligence  
- Charisma  

Each attribute is independently generated, ensuring a fair distribution of stats.  

How to Play:  
1. The program rolls four six-sided dice for each attribute.  
2. It removes the lowest die roll and sums the remaining three.  
3. The attributes are assigned to two players for character creation.  
4. The generated stats are displayed in a structured format.  

This program provides a quick and reliable way to generate **balanced character stats**  
for a new D&D adventure.  
"""

import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    die4 = random.randint(1, 6)
    minimum = min(die1, die2, die3, die4)
    total = die1 + die2 + die3 + die4 - minimum
    return total

def generate_stats():
    strength = roll_dice()
    constitution = roll_dice()
    dexterity = roll_dice()
    wisdom = roll_dice()
    intelligence = roll_dice()
    charisma = roll_dice()
    display_stats(strength, constitution, dexterity, wisdom, intelligence, charisma)
    return strength, constitution, dexterity, wisdom, intelligence, charisma

def display_stats(strength, constitution, dexterity, wisdom, intelligence, charisma):
    print("Strength:", strength)
    print("Constitution:", constitution)
    print("Dexterity:", dexterity)
    print("Wisdom:", wisdom)
    print("Intelligence:", intelligence)
    print("Charisma:", charisma)

# MAIN PROGRAM ========================

print("Player :")
strength1, constitution1, dexterity1, wisdom1, intelligence1, charisma1 = generate_stats()


strength2, constitution2, dexterity2, wisdom2, intelligence2, charisma2 = generate_stats()
