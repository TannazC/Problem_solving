"""
This program counts the number of words in a given string, ensuring that each word contains at least three or more characters.

The get_string(case, prompt) function collects a validated string input, ensuring it contains only letters and has at least three characters.
The wordcount() function converts the string to lowercase and calculates the number of words based on spaces (" ") between them.
This function is useful for basic text processing tasks, such as analyzing word counts in user input or validating formatted string entries.

*this can be imported as a function in larger programs*

"""

def get_string(case,prompt):
    choice = input(prompt)
    choice=choice.strip(" ")
    while not choice.isalpha() or len(choice)<=3 :
        choice = int(input("Invalid input, try again: "))
    if case=="up" or cause=="UP":
        choice=choice.upper()
    elif case=="low" or cause=="LOW":
        choice=choice.lower()
    return choice


def wordcount():
    string= get_string("low","Input random string of words: ")
    Words= (string.count(" "))+1
    return Words
    
