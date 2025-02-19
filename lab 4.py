import math

"""
Problem 1: Series Sum using a for Loop
What it does:

Computes a mathematical series sum using 500 iterations.
Each term alternates in sign and is calculated as ((-1)^i) * (2*i+1) / i.
The final result is stored in series_sum.
"""

series_sum = 0
N= 500
for i in range(1,N+1):
    term = ((-1)**i)*(2*i+1)/i
    series_sum += term
    
"""
Problem 2: Series Sum using a while Loop
What it does:

Performs the same computation as Problem 1, but using a while loop instead of a for loop.
Iterates from 1 to 500, computing the sum term by term.
"""

series_sum = 0
N= 500
i=1
while i<=N:
    term = ((-1)**i)*(2*i+1)/i
    series_sum += term
    i+=1
    

''' 
Problem 3: Greatest Common Divisor (GCD) using Brute Force
Finds the greatest common divisor (GCD) of two numbers using exhaustive search.
Starts from the larger number and decrements until it finds the largest divisor common to both numbers.
Returns 0 if there is no valid divisor.

Remainder = Dividend – (Divisor × Quotient)
// -->quotient
% -->remainder 
'''

def gcd(n,m):
    if n>m:
        num = n
    else:
        num = m
    
    while True and num>0:
        num-=1
        if num<=0:
            return 0
        if  n - ((num)*(n//num)) == 0 and m - ((num)*(m//num)) == 0:
            return num     
        


'''
Problem 4: Simplifying a Fraction
Uses gcd(n, m) to compute the greatest common divisor (GCD).
Divides both the numerator and denominator by the GCD to simplify the fraction.
If the fraction results in a whole number, it prints the integer value instead of a fraction.
'''

def simplify_fraction(n, m):
    great = gcd(n,m)
    n_new = int(n / great)
    m_new = int(m / great)
    if (n/m) - int(n/m) == 0 :
        print(n/m)
        return
    else:
        print( n_new," /", m_new)
        return
    
"""
Problem 5: Collecting and Printing a List of Names
What it does:

Continuously asks the user for names until "END" is entered.
Stores names in a list and formats them into a comma-separated string for display.
Outputs the full list of names at the end.
"""

names = []
new_name = " " 

while new_name!= "END":
    new_name = input(" input a name or END to stop: " )
    names.append(new_name)
    
    
names_print = ""
for i in names:
    if i == "END":
        pass
    names_print+= str(i)
    names_print+= ", "
    
print("The names are : ", names_print)

"""
Problem 6: Approximating π using the Gregory-Leibniz Series
What it does:

Uses the Gregory-Leibniz series to approximate the value of π.
Keeps iterating until the computed value matches math.pi rounded to n decimal places.
"""

pii = 0
n= 1
i=0
while round(pii*4,n) != round((math.pi),n):
    term =((-1)**i)/(2*i+1)
    pii += term
    i+=1

print(pii*4) 

"""
Problem 7: Finding the Next Day in a Date
Part (a): next_day(y, m, d)
What it does:

Determines if the given year is a leap year.
Increments the day, month, or year based on the month’s number of days.
Handles leap year adjustments for February.
Outputs the next day's date in a readable format.

Part (b): Counting Days Between Two Dates
What it does:
(Incomplete) Intended to iterate through all dates between two given dates, printing each one.
Uses next_day() to compute the next day in sequence.
"""

#part a)
def next_day(y, m , d):
    #check if leap year
    if y%4 == 0:
        leap_year = True
        
    else:
        leap_year = False
    
    #check month (31 days)
    if m in [1, 3, 5, 7, 8, 10, 12]:
        daycount = 31
        if d == daycount and m == 12:
            m= 1
            d=1
            y+=1
        elif d == daycount and m!=12:
            m+=1
            d=1
        else:
            d+=1
    #check month (28/29 days)
    elif m == 2:
        if leap_year == True:
            daycount = 29
        else:
            daycount = 28
    
        if d == daycount and m == 12:
            m= 1
            d=1
            y+=1
        elif d == daycount and m!=12:
            m+=1
            d=1
        else:
            d+=1
    #check month (30 days)
    else:
        daycount = 30
        if d == daycount and m == 12:
            m= 1
            d=1
            y+=1
        elif d == daycount and m!=12:
            m+=1
            d=1
        else:
            d+=1
        
    months = ["January","February","March","April","May","June","July","August","Septmember","October","November","December"]
    month = months[m-1]
    
    print(month,d,",",y)
    newd = d
    newy = y
    newm = m
    return newd, newy, newm

#part b)
def counting_days(d1, m1, y1, d2, m2, y2):

    # Ensure the first date is earlier than the second
    if (y1, m1, d1) > (y2, m2, d2):
        d1, m1, y1, d2, m2, y2 = d2, m2, y2, d1, m1, y1

    days_count = 0
    current_d, current_m, current_y = d1, m1, y1

    while (current_y, current_m, current_d) < (y2, m2, d2):
        print(f"{current_y}/{current_m}/{current_d}")  # Print the current date
        current_d, current_y, current_m = next_day(current_y, current_m, current_d)
        days_count += 1

    print(f"{y2}/{m2}/{d2}")  # Print the final date
    return days_count


"""
Problem 8: Advanced GCD Algorithm
What it does:

Uses the Euclidean Algorithm to compute the greatest common divisor (GCD).
Continues swapping and dividing the two numbers until the remainder is 0, at which point it returns the GCD.   
"""
def gcd_advanced(n,m):
    if m>n:
        n = m, m = n
    
    while True:
        n = m, m = n%m
        if n%m == 0:
            return m
        
    
    
    
