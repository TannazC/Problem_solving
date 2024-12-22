#Read a string consisting entirely of letters from the user, then determine its “score” using the
#following rules:
#• each letter has a value determined by its position in the alphabet (e.g. A=1, Z=26)
#• each letter’s value is multiplied by the value of its position in the string (e.g. second letter x2)
#For example, the word “dog” would have a score of 4x1 + 15x2 + 7x3 = 55. Your program should
#handle both lower- and uppercase input.


word=(input("enter a word: ")).upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
totalscore=0
x="x"
for letter in word:
        score = ((alphabet.find(letter))+1)*((word.find(letter))+1)
        print( f"{((alphabet.find(letter))+1):<}{x:^}{((word.find(letter))+1):>}")
        totalscore+=score

print("'",word,"' has a score of: ", totalscore)

#print(f"{index:[[fill]align][sign][width][grouping][.precision][type]}")