# One method of creating a character in D&D involves rolling
# four six-sided dice and taking the three largest values.
# These values are added together to form one of six attributes:
# strength, constitution, dexterity, wisdom, intelligence and
# charisma. Write a program that randomly generates a character's
# stats, so they can be used to play a game.
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