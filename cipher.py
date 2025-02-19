"""
Caesar Cipher Encryption and Decryption  
Author: Tannaz Chowdhury  
GitHub: TannazC  
Date: 2023  

Description:  
This program implements the **Caesar Cipher**, a simple substitution cipher used for encryption and decryption.  
It shifts each letter in the message forward or backward by a specified key value.  

How It Works:  
1. The user chooses whether to **encrypt or decrypt** a message.  
2. The user enters the **message** to be processed.  
3. A **key value (1 to 52)** is selected, determining how many positions each letter is shifted.  
4. The program **encrypts or decrypts** the message based on the key and displays the result.  

Encryption Example (Key = 3):  
- Plaintext: `HELLO` → Ciphertext: `KHOOR`  

Decryption Example (Key = 3):  
- Ciphertext: `KHOOR` → Plaintext: `HELLO`  

This program demonstrates **basic cryptography concepts** and the use of **string manipulation, loops, and user input validation**.  
"""

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # Symbol not found in SYMBOLS.
            # Just add this symbol without any change.
            translated += symbol
        else:
            # Encrypt or decrypt
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
