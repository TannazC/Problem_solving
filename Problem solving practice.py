'''Write a function that takes the number n and returns a list of all the perfect squares between
0 and n. A perfect square is a number s such that k2 = s for some integer k. For example, get perfect squares(36)
should return the list [0, 1, 4, 9, 16, 25, 36]'''

def get_perfect_squares(n):
    list = []
    for i in range(0,n+1):
        if i*i<=n:
            list.append(i*i)
        else:
            continue
    print(list)
        
'''Write a function that computes the product of the elements of a list of integers.
For example, prod([2, 3, 4]) should return 24, since 2 × 3 × 4 = 24.'''
def prod(L):
    prod = 1
    for elm in L:
        prod*=elm
    print(prod)

prod([2,3,4])

'''Write a function with the signature duplicates(list0),
which returns True iff list0 contains at least two
adjacent elements with the same value.'''

def duplicates(list0):
    for i in range(1, len(list0)):
        if list0[i] == list0[i - 1]:
            return True
    return False

'''Recall that a matrix can be stored as a list of lists. For example, the matrix
5 0 0
0 0 1 
can be stored as [[5, 0, 0], [0, 0, 1]]
Write a function that takes in two matrices stored as lists of lists of numbers, and returns the
sum of the two matrices, stored as a list of lists.
If the two matrices cannot be added because of a dimension
mismatch, return the string "ERROR".'''
def matrix_sum(A, B):

    #if rows and columns match
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        #create a sum matrix
        sum_matrix = []
        
        #for 2 rows
        for i in range(0,len(A)):
            #create 2 rows
            sum_matrix.append([])
            #for 3 columns
            for j in range(0,len(A[0])):
                #create a sum for each
                sum_matrix[i].append( (A[i])[j]+(B[i])[j] )
    else:
        return 
    return sum_matrix, print(sum_matrix)

A = [[5, 0, 0], [0, 0, 1]]
B = [[5, 0], [0, 0,]]

matrix_sum(A,B)



'''Consider the following dictionary that contains the
information on which kids got which candy in which
house:
halloween_haul = {"house1": {"Annie": ["snickers", "mars"],
"Johnny": ["snickers"] },
"house2": {"Annie": ["coffee break", "mars"],
"Jackie":["coffee break"]}
}
Write a function that takes in a dictionary in a format
like the above and returns the name of the kid who collected the most candy items.
For example luckiest_kid(halloween_haul) should return "Annie", since
Annie collected 4 candy items in total. The input dictionary can have
any number of houses, any number of kids, and any number of different
candy items. Assume that there is just one kid
who collected the most candy items.'''
def luckiest_kid(haul_dataset):
    # Dictionary to store total candy count for each kid
    candy_count = {}

    # Loop through each house, acess kid
    for house, kids in haul_dataset.items():
        # Loop through each kid in the house, acess candy
        for kid, candies in kids.items():
            # If the kid is already in the dictionary, add to their count
            if kid in candy_count:
                candy_count[kid] += len(candies)
            else:
                # If the kid is not in the dictionary, add them with the initial candy count
                candy_count[kid] = len(candies)

    # Find the kid with the most candies
    luckiest_kid = max(candy_count, key=candy_count.get)

    return luckiest_kid


Part (a) [3 marks]
def f(L):
    global L
    L = [1, 2, 3]
    L[0] = 5
    print(L[0])
    L1 = [4, 5, 6]
    f(L1)
    print(L)
    print(L1)
    Output:

            
'''Write a function that finds the element that occurs the most frequently in a given list of strings.
For example, most_frequent(["candy", "costumes", "midterms", "candy"]) should return "candy", since
"candy" appears twice in the list of strings, which is more than any other string in the list.Assume there
are no “ties”. You may not import any modules (like in other questions), but may otherwise use any
functionality available in Python. You may use helper functions. Hint: one way (but not the only way)
to start solving this problem is to count how many times "candy" appears and check if it appears more
times than any other string in the list, etc.'''
def most_frequent_fave(faves):
    frequency = {}
    
    for i in faves:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i] = 1
            
    largest_key = max(frequency, key=frequency.get)
    return largest_key, print(largest_key)

faves = ["candy", "costumes", "midterms", "candy"]
most_frequent_fave(faves)




'''Write code that would allow a user to call the function check next prime as follows:
check_next_prime(2) # print "Correct"
check_next_prime(3) # print "Correct"
check_next_prime(4) # print "Incorrect, game over"
check_next_prime(5) # print "Game is over"
The function prints Correct while the user call the function using prime numbers in the order 2, 3, 5,
7, 11, ...
The first time the user enters an unexpected number (e.g., 5), the function prints Incorrect, game over.
After printing this message, the function only ever prints "Game is over", no matter what the user enters.
Your answer should include the definition of the function, as well as any other code needed to make
the code work.
'''               
            

'''A =

1 2 4
2 5 3
4 3 9'''



def is_almost_symmetric(M):
    # Step 1: Check if the matrix is square (necessary condition for symmetry)
    n = len(M)
    for row in M:
        if len(row) != n:
            return False  # Not a square matrix

    # Step 2: Find all mismatches where A[i][j] != A[j][i]
    mismatches = []
    for i in range(n):
        for j in range(i + 1, n):  # Only need to check above the diagonal (column 2 to start)
            if M[i][j] != M[j][i]: 
                mismatches.append((i, j))

    # Step 3: If no mismatches, the matrix is already symmetric
    if not mismatches:
        return True

    # Step 4: If exactly two mismatches, check if swapping fixes the symmetry
    if len(mismatches) == 2:
        (i1, j1), (i2, j2) = mismatches
        # To make it symmetric, we must be able to swap the mismatched elements
        # i.e., M[i1][j1] should equal M[i2][j2] and M[j1][i1] should equal M[j2][i2]
        if (i1, j1) == (j2, i2) and M[i1][j1] == M[j2][i2] and M[i2][j2] == M[j1][i1]:
            return True
    
    # Step 5: If not exactly two mismatches or swapping doesn't fix the matrix, return False
    return False


B = [[1, 2, 4], [2, 5, 9], [4, 3, 3]]
print(is_almost_symmetric(B))
    
    
        
        