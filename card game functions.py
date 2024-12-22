#CARD GAME FUNCTIONS

#make_deck: creates a list containing the 52 cards (4 suits of 13 cards each) if a standard deck.
#You should choose a method of storing both the rank (e.g. Jack) and suit (e.g. Hearts) of each
#card. Popular methods include strings, such as "Jack of Hearts" or "JH", or tuples, such as
#("Jack", "Hearts") or (11, 2). Use some form of loop to build the deck, rather than
#specifying all cards manualy. Return the deck of cards.

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

#shuffle_deck: randomly arranges the cards in the deck. As an exercise, try to do this without
#using the random module’s shuffle method. Return the shuffled deck.

import random
def shuffle(deck):
    random.shuffle(deck)
    return deck

#deal_card: remove one card from the top of the deck. Return that card, so it can be used in the
#main program.

def deal_card(deck):
    deck.reverse()
    card=deck.pop()
    return card


#make_hand: remove n cards from the top of the deck and create a list representing a player’s
#hand. Try to use your deal_card function to reduce code. Return the hand.

def make_hand(n,deck):
    hand=[]
    for count in range(0,n):
        card= deal_card(deck)
        hand.append(card)
    return hand
    
#play_card: remove one card from a player’s hand. Return that card, so it can be used in the
#main program. You will need to pass arguments to this function that will be able to identify a
#card that is in the player’s hand. Do not ask for the user to select the card in this function.

def play_card(hand):
    newcard=random.choice(hand)
    return newcard
    

#get_card_name: obtain the name of a card. For example, if a card is represented as "JH", your
#function should return "Jack of Hearts". Return the card as a string.

def get_card_name(short_name):

    suit={"H","S","D","C"}
    rank={"A","K","Q","J","10","9","8","7","6","5","4","3","2","1"}
    deck= get_named_deck(suit,rank)
    print(deck)
    suit={"Hearts","Spades","Diamonds","Clubs"}
    rank={"Ace of ","King of ","Queen of ","Jack of ","10 of ","9 of ","8 of ","7 of ","6 of ","5 of ","4 of ","3 of ","2 of ","1 of "}
    name= get_named_deck(suit,rank)
    print(name)
    newname=name[deck.index(short_name)]
    return newname


#print_cards: displays the names of all cards in a given hand or deck. Call your
#get_card_name function here. This function does not need to return a value.
