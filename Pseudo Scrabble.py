#Generate 10 random “words” of 3-8 letters each. Each letter is worth a certain
#number of points: 3 for the letters “X”, “Y” or “Z”, 2 for any other consonant, and 1 for a vowel.
#Display each word, along with the total number of points in the word (e.g. “BXAL [6 points]”), then
#determine the total number of points from all 10 words.
import random
word = "'"
for count in range(0,10):
    points=0
    numberofletters=random.randint(3,9)
    for letter in range(1,numberofletters):
        inletter=random.choice("ABCDEFGHIJKLMNOPXRSTUVWXYZ")
        word += inletter
    for let in word:
        if let=="X" or let=="Y" or let=="Z":
            points+=3
        elif let=="A"or let=="E"or let=="I"or let=="U"or let=="O":
            points+=1
        else:
            points+=2    
    finalpoints=points-1
    print(word,"[",finalpoints," points ]")
    word = "'"
        
