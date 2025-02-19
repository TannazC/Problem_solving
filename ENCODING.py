"""
Vigenère Cipher Encoder  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program encrypts a message using the **Vigenère Cipher**, a method of polyalphabetic  
substitution encryption. The cipher shifts each letter in the plaintext based on a repeating  
keyword, making it more secure than simple shift ciphers like **Caesar Cipher**.  

How It Works:  
1. The user inputs a **plaintext message**, which is converted to **uppercase**.  
2. The user enters a **keyword** (must be at least 3 letters long).  
3. The keyword is **repeated** to match the length of the plaintext.  
4. Each letter in the plaintext is shifted based on the corresponding letter in the key.  
5. Non-alphabetic characters remain unchanged.  
6. The encrypted message is displayed.  

This program demonstrates string manipulation, input validation,  
and classical cryptographic techniques in Python.  
"""

# Get the plaintext (any characters, converted to uppercase)
plaintext = input("Plaintext: ").upper()
ptlen = len(plaintext)

# Get a valid key (all letters, at least 3 characters long)
key = ""
while not key.isalpha() or len(key) < 3:
    key = input("Key: ").upper()
keylen = len(key)

# Build the keytext (make it larger than needed, then trim it)
keytext = key * (ptlen // keylen + 1)
keytext = keytext[:ptlen]

# Set some values for encryption
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = ""

# loop through each character in the plaintext and keytext
for idx in range(ptlen):

    # character is a letter -- encrypt it
    if plaintext[idx] in alphabet:
 
        # add the plaintext and key values together
        # (offshift 1 for index)
        ptval = alphabet.find(plaintext[idx]) + 1
        ktval = alphabet.find(keytext[idx]) + 1
        newval = ptval + ktval
 
        # subtract 26 if resulting value is too large
        if newval > 26:
            newval -= 26
 
        # set the new character (offshift 1 for index)
        ciphertext += alphabet[newval - 1]
 
    # character is not a letter -- skip it
    else:
        ciphertext += plaintext[idx]

print("The encrypted message is '{}'.".format(ciphertext))
