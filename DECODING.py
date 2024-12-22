#DECODING

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