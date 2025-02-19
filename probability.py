"""
This program provides functions for calculating permutations, combinations, and binomial probability distributions.

The permutations(n, r) function computes the number of ways to arrange r elements from a set of n.
The combinations(n, r) function calculates the number of ways to choose r elements from n, disregarding order.
The binomial_pd(n, x, p) function computes the binomial probability distribution, determining the probability of x successes in n trials given a success probability p.
"""

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
