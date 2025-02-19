"""
This program validates Canadian postal codes, ensuring they adhere to the A1A 1A1 format, where:

The code consists of exactly six characters (no spaces).
Letters and numbers alternate (e.g., A1B2C3).
The first letter cannot be 'W' or 'Z', as these are not used in Canadian postal codes.
Letters D, F, I, O, Q, and U are not permitted in any letter position.
"""

def postalcode():
    
    postal=input("Enter a valid code: ")
    postal=postal.strip(" ")
    let=str(postal[0::2]).upper() 
    num=str(postal[1::2])
    
    if (len(postal)==6):
        if (let.isalpha() and num.isdigit()):
            if (let[0]!="W" and let[0]!="Z"):
                for cha in let:
                    if cha in "DFIOQU":
                        return False
                    else:
                        continue 
            else:
                return False
        else:
            return False 
    else:
        return False
    
    return True


if postalcode():
    print("Valid")
else:
    print("Invalid")
