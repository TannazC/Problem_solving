"""
Vigenère Cipher Decoder  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program decrypts a message encrypted with the **Vigenère Cipher**,  
a polyalphabetic substitution cipher that shifts letters based on a keyword.  
By reversing the encryption process, the original plaintext is recovered.  

How It Works:  
1. The user inputs the **ciphertext** (encrypted message), which is converted to **uppercase**.  
2. The user enters a **keyword** (must be at least 3 letters long).  
3. The keyword is **repeated** to match the length of the ciphertext.  
4. Each letter in the ciphertext is **shifted backward** based on the corresponding letter in the key.  
5. Non-alphabetic characters remain unchanged.  
6. The decrypted plaintext is displayed.  

This program demonstrates **string manipulation, input validation, and classical decryption  
techniques** used in historical cryptography.  
"""


ciphertext = input("ciphertext: ").upper()
cplen = len(ciphertext)

key = ""

while not key.isalpha() or len(key) < 3:
    key = input("Key: ").upper()
keylen = len(key)

keytext = key * (cplen // keylen + 1)
keytext = keytext[:cplen]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = ""

for idx in range(0,cplen):

    if ciphertext[idx] in alphabet:
#------------------------------
        cpval = alphabet.find(ciphertext[idx])
        ktval = alphabet.find(keytext[idx]) 
        
        if (cpval+26)-ktval < 26:
            cpval += 26
        
        newval= cpval-ktval

        plaintext += alphabet[newval-1]
#-----------------------------

    else:
        plaintext += ciphertext[idx]

print("The DE-encrypted message is '{}'.".format(plaintext))

#Plaintext: HELLO
#Key: CAT
#The encrypted message is 'KFFOP'.
