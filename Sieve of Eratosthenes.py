#Here is an ancient method for generating prime numbers less than n. Start
#with a list of numbers from 0 to n-1. Since neither 0 nor 1 are prime, cross them off. 2 is the
#smallest prime number. Cross off all multiples of 2 in the list that are greater than 2. Find the next
#value in the list that has not been crossed off. In this case, this is 3. This value is prime. Cross off all
#multiples of 3 that are greater than 3. Find the next value in the list that has not been crossed off.
#In this case, this is 5. Cross of multiples of 5 greater than 5, etc. Repeat until it is not possible to
#find a next uncrossed value. Use the list and range functions to create a list containing the
#values from 0 to n-1, then perform the steps above to mark all non-prime numbers from the list.
#Print the remaining prime numbers.

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
