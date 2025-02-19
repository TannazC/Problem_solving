"""
Inappropriate Language Censorship Program  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This program censors inappropriate words in a given sentence by replacing them with  
polite alternatives. It scans the input text, checks for occurrences of words from a  
predefined "banned words" list, and replaces them with their corresponding substitutes  
from a replacement list.  

How It Works:  
1. The user inputs a sentence.  
2. The program checks for any inappropriate words in the sentence.  
3. If a word from the censorship list is found, it is replaced with its polite alternative.  
4. If the word appears multiple times, the program replaces all occurrences.  
5. The modified sentence is displayed.  

This program demonstrates string manipulation, list indexing, and text replacement,  
making it useful for chat filtering, content moderation, and text processing applications.  
"""

string=input("Enter a sentance: ")

curse=["damn", "hell"]
replace=["dang","heck"]

for word in curse:
    if word in string and string.count(word)==1:
        curse_pos=curse.index(word)
        new=replace[curse_pos]
        str_pos=string.find(word)
        newstr=string[0:str_pos]+new+string[str_pos+len(new):]
        string=newstr
    elif word in string and string.count(word)>1:
        for instance in range(0,string.count(word)):
            curse_pos=curse.index(word)
            new=replace[curse_pos]
            str_pos=string.find(word)
            newstr=string[0:str_pos]+new+string[str_pos+len(new):]
            string=newstr
           

print(newstr)
