#Card Selector: Generate a list of five different playing cards (you may choose how to represent
#them). Display the user’s hand in a nicely-formatted manner. Ask them which card (1-5) they
#would like to play, then remove that card from their hand. Display the new hand. Remember that
#lists in Python are zero-indexed!

import inval
import random

def generate_hand():
    hand=[]
    for count in range(0,5):
        options=["heart","spade","diamond","club","jack"]
        card= random.choice(options)
        hand.append(card)
    return hand

hand=generate_hand()
print(f"{hand}")

def play_hand(hand):
    choice=inval.get_string(prompt="Enter the card you want to play: ",case="low")
    pos=hand.index(choice)
    newstr=[]
    for count in range(len(hand)):
        if count==pos:
            continue
        else:
            newstr.append(hand[count])
    
            
    return newstr


hand=play_hand(hand)
print(f"{hand}")
    
