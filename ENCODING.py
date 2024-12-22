
#ENCODING


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
