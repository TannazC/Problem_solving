"""
Letter Scoring Program  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: [2023]  

Description:  
This program calculates the "score" of a given word based on letter values and their  
positions in the string. Each letter’s score is determined by:  
- **Alphabet Position:** A=1, B=2, ..., Z=26  
- **Positional Multiplier:** Each letter’s value is multiplied by its position in the word  

For example, the word "DOG" has a score calculated as:  
  (D=4 × 1) + (O=15 × 2) + (G=7 × 3) = **55**  

How to Use:  
1. Enter a word containing only **letters**.  
2. The program converts it to uppercase for uniform scoring.  
3. It computes the total score based on letter positions.  
4. The final score is displayed.  
"""


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
