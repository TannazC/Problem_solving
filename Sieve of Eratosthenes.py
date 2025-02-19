"""
Ancient Prime Number Generator (Sieve of Eratosthenes)  
Author: Tannaz Chowdhury  
Date: 2023  

Description:  
This program generates all prime numbers **less than a given number n** using  
an ancient method similar to the **Sieve of Eratosthenes**. It systematically eliminates  
non-prime numbers by marking multiples of each discovered prime.  

How It Works:  
1. A list of numbers from **0 to n-1** is created.  
2. The numbers **0 and 1** are **crossed off** as they are not prime.  
3. The program iterates through the list:  
   - If a number is not crossed off, it is prime.  
   - All multiples of that prime greater than itself are marked as non-prime.  
4. The process repeats until no more unmarked numbers remain.  
5. The program prints the **remaining prime numbers** in order.  

This program efficiently demonstrates **prime number detection, list operations,  
and mathematical pattern recognition**.  
"""


import inval
import math

def ancient_prime_method(n):
    primes = []
    numbers = list(range(n))

    # Cross off 0 and 1
    numbers[0] = None
    numbers[1] = None

    # Mark multiples of each prime as non-prime
    for i in range(2, n):
        if numbers[i] is not None:
            primes.append(numbers[i])
            for j in range(i, n, numbers[i]):
                numbers[j] = None

    # Print the remaining prime numbers
    print("Prime numbers less than", n, ":")
    for prime in primes:
        print(prime)


# Prompt the user for the value of n
n = int(input("Enter a number (n): "))

# Generate prime numbers using the ancient method
ancient_prime_method(n)
