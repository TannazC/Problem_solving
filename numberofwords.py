

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
    
#Count the number of “words” in a given string that contain three or more characters.
