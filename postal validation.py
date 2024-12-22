
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