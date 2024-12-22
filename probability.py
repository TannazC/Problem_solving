import math

def permutations(n,r):
    
    if r>n:
        return 0
    elif r<0 or n<0:
        return 0
    
    perms=int((math.factorial(n))/(math.factorial(n-r)))
    return perms 

def combonations(n,r):
    
    if r<0:
        return 0
    
    perms= permutations(n,r)
    combos= perms/(math.factorial(r))
    return combos

def binomial_pd(n,x,p):
    
    binom=(combonations(n,x)) * (p**x) * ((1-p)**(n-x))
    return binom
