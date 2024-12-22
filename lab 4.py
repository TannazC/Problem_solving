import math

#problem 1
series_sum = 0
N= 500
for i in range(1,N+1):
    term = ((-1)**i)*(2*i+1)/i
    series_sum += term
    
'print(series_sum)'

#problem 2

series_sum = 0
N= 500
i=1
while i<=N:
    term = ((-1)**i)*(2*i+1)/i
    series_sum += term
    i+=1
    
'print(series_sum)'

#problem 3
'''The greatest common divisor of n and m is a number d such that n is divisible by d and m is divisible
by d.
Note that k is divisible by d if and only if the remainder of the division of k by d is 0, i.e., k % d == 0.
There is an efficient algorithm for doing finding the greatest common divisor (more on this later),
but in this question, you should use exhaustive search: trying every possible answer until you find the
right one. This is a similar approach to the one we used for is perfect square in the Monday lecture

Remainder = Dividend – (Divisor × Quotient)
// quotient
% remainder '''



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
        
'print(gcd(500,10))'


#problem 4
'''Write a function with the signature simpify_fraction(n, m) which prints the simplified version of the
fraction n
m
.
Note that we asked you to print, not return. That is because we don’t yet have a mechanism to return
more than one number.
You do not need to use a complicated algorithm to compute the greatest common divisor (although
you certainly can do that!). For example, simplify_fraction(3,6) should print 1/2, and
simplify_fraction(8, 4) should print 2.'''

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
    
'print(simplify_fraction(10,2))'

#problem 5

'''Write a program that reads repeatedly asks the user for names, and then outputs the list of all the names
before the special name END is entered. An example of an interaction would be:
Enter a name: Alice
Enter a name: Bob
Enter a name: Charlie
Enter a name: Dave
Enter a name: Emily
Enter a name: END
The names are: Alice, Bob, Charlie, Dave, Emily
To store the names in the program, you can use a string. For example, the string might be "" at first,
then "Alice", then "Alice, Bob", etc. You can use the += operator to add a name to the string.'''
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

#problem 6

pii = 0
n= 1
i=0
while round(pii*4,n) != round((math.pi),n):
    term =((-1)**i)/(2*i+1)
    pii += term
    i+=1

print(pii*4) 

#problem 7
'''
 Write a function with the signature next_day(y, m , d) which prints the date that follows the date
y/m/d.
Reminder:
According to the Gregorian calendar, which is the civil calendar in use today, years evenly
divisible by 4 are leap years, with the exception of centurial years that are not evenly divisible
by 400. Therefore, the years 1700, 1800, 1900 and 2100 are not leap years, but 1600, 2000, and
2400 are leap years. (Source: the US Naval Observatory website.)

'''
#part a

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
    
#next_day(2024, 2, 28)

'''
Part (b) Counting Days

Write a function that prints out, in order, all the dates between fY/fM/fD and tY/tM/tD. Using the same
idea, write a function that returns the number of days between two dates '''
'''
def counting_days(d1,m1,y1,d2,m2,y2):
    while d!=d2 and m!=m2 and y!=y2:
        next_day(y1,m1,d1)
        
        
        

counting_days(21,3,2006,30,3,2006)
'''


    
def gcd_advanced(n,m):
    if m>n:
        n = m, m = n
    
    while True:
        n = m, m = n%m
        if n%m == 0:
            return m
        
    
    
    