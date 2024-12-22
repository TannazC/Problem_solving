
#CARD GAME FUNCTIONS
def make_deck(suit,rank):
    deck=[]
    for colour in suit:
        for types in rank:
            deck.append((types,colour))
    deck.sort()
    return deck

def get_named_deck(suit,rank):
    deck=[]
    for colour in suit:
        for types in rank:
            name= str(types)+str(colour)
            deck.append(name)
    deck.sort()
    return deck

import random
def shuffle(deck):
    random.shuffle(deck)
    return deck

def deal_card(deck):
    deck.reverse()
    card=deck.pop()
    return card

def make_hand(n,deck):
    hand=[]
    for count in range(0,n):
        card= deal_card(deck)
        hand.append(card)
    return hand

def play_card(hand):
    newcard=random.choice(hand)
    return newcard

def get_card_name(short_name):

    suit={"H","S","D","C"}
    rank={"A","K","Q","J","10","9","8","7","6","5","4","3","2","1"}
    deck= get_named_deck(suit,rank)
    
    suit={"Hearts","Spades","Diamonds","Clubs"}
    rank={"Ace of ","King of ","Queen of ","Jack of ","10 of ","9 of ","8 of ","7 of ","6 of ","5 of ","4 of ","3 of ","2 of ","1 of "}
    name= get_named_deck(suit,rank)
  
    newname=name[deck.index(short_name)]
    return newname

def print_hand(hand):
    for elm in hand:
        card=get_card_name(elm)
        print(card)

import inval

#================================================ MAIN PROGRAM - GO FISH

#suit={"Hearts","Spades","Diamonds","Clubs"}
#rank={"Ace of ","King of ","Queen of ","Jack of ","9 of ","8 of ","7 of ","6 of ","5 of ","4 of ","3 of ","2 of ","1 of "}
#deck=get_named_deck(suit,rank)

suit={"H","S","D","C"}
rank={"A","K","Q","J","9","8","7","6","5","4","3","2","1"}
deck= get_named_deck(suit,rank)

shuffle(deck)

hand1= make_hand(8,deck)
hand2= make_hand(8,deck)
wins1=[]
wins2=[]
wins=wins1

player=1
hand=hand1
other_hand=hand2
throw=[]



while True:
    
    print(f"PLAYER {player} ================")
    print(print_hand(hand))
    
    #CARD VALIDATION
    card_request=(input("Enter the card abreviation of what you want: "))
    
    #INCREASED VALIDATION ***** FULL NAMES 
    
    while (card_request in hand) or (card_request in throw):
            card_request=(input("Enter the card abreviation of what you want: "))
    
    #gofish
    if card_request in other_hand:
        print("You got it!")
        hand.append(card_request)
        other_hand.remove(card_request)
    else:
        print("Go fish!")
        hand.append(deal_card(deck))
    
    #stacks
    new_hand=[]
    rep=[]
    for elm in hand:
        new_hand.append(elm[0])
        rep.append(elm)


    for numb in "QA123456789JK":
        if  (numb in new_hand) and (new_hand.count(numb)==4):
            for card in rep:
                if numb in card:
                    hand.remove(card)
                    throw.append(card)
                    wins.append(str(numb))
            print(f"You got a stack of {numb}s!")
                    
    #empty deck    
    if len(deck)==0 and len(hand1)==0 and len(hand2) ==0:
        break
    
    #switch player and variables
    if player==2:
        player=1
        wins=wins1
        hand=hand1
        other_hand=hand2
    else:
        player=2
        wins=wins2
        hand=hand2
        other_hand=hand1   
        

#who won with stacks
wins1=len(set(wins1))
wins2=len(set(wins2))

if wins1>wins2:
    winner=1
    points=wins1
else:
    winner=2
    points=wins2
    
print(f"Player {winner} wins with {points}")



