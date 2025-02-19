#Python problem-solving practice labs

'''Problem 1.
Download numpy.py and understand how to print lists of lists as matrices by converting lists of lists to
arrays (lines 1-11). Write a function print_matrix(M_lol) which prints the nested list M_lol as a matrix.
You will be able to use your function to debug your implementation of Gaussian Elimination.'''



def print_matrix(M_lol):
    for row in M_lol:
        print(" ".join(f"{elem}" for elem in row))  # format each element to 2 decimal places for readability
    print()  # Adds a newline for spacing
    
    M_lol = np.array(M_lol)
    print(M_lol)


'''Problem 2.
Write a function with the signature get_lead_ind(row) which takes in a list of numbers row, and returns
the index of the first non-zero element of row. The function should return len(row) if the row contains
no non-zero elements.'''


def get_lead_ind(row):
    if 0 not in row:
        return len(row)
    else:
        for entry in row:
            if entry!= 0 :
                return row.index(entry)
'''Problem 3.
Write a function with the signature get_row_to_swap(M, start_i) which takes in a matrix M (represented
as a list of lists) and an integer start_i, and returns the row that needs to be swapped (permuted/interchanged) with the row M[start_i]. The row that needs to be swapped with the row M[start_i] is the
row at index larger or equal to start_i which has the leading non-zero coefficient that is as far to the left
as possible.
For example, for
M = [[5, 6, 7, 8],
[0, 0, 0, 1],
[0, 0, 5, 2],
[0, 1, 0, 0]]
start_i = 1,
[0,0, 0, 1] needs to be swapped with [0, 1, 0, 0], so that the function should return 3.

Finds the row index with the leading non-zero coefficient that is farthest to the left
    among the rows from start_i onward, and returns the index of that row.

    Args:
        M (list of list of floats): The matrix represented as a list of lists.
        start_i (int): The starting row index to consider for swapping.

    Returns:
        int: The index of the row that should be swapped with M[start_i].'''

            
def get_row_to_swap(M, start_i):
    min_lead_index = len(M[start_i]) # there is no leading 0, length
    row_to_swap = start_i #rename ugly variable name

    for i in range(start_i, len(M)): # look at rows below to swap ; ARRANGING IN ORDER OF LEADING 0, compare
        lead_index = get_lead_ind(M[i])  # Get the leading non-zero index of the row
        if lead_index < min_lead_index: 
            min_lead_index = lead_index
            row_to_swap = i

    return row_to_swap


'''Problem 4.
Write a function with the signature add_rows_coefs(r1, c1, r2, c2) which takes in rows (represented
as lists of equal lengths) r1 and r2 and coefficients (floats) c1 and c2, and returns a new list that contains
the row c1*r1 + c2*r2. (N.B.: to create a new list of 10 zeros, you can use [0]*10.)'''

def add_rows_coefs(r1, c1, r2, c2):
    return [c1 * r1[i] + c2 * r2[i] for i in range(len(r1))] #adding coeficients for each row of length r1, returns list added

print(add_rows_coefs([1,2,3], 2, [-2,-4,-6], 1))

'''Problem 5.
Write a function with the signature eliminate(M, row_to_sub, best_lead_ind) which takes in a matrix
M (represented as a list of lists),
row_to_sub, an index of the row to subtract from other rows to eliminate,
and best_lead_ind, the index of the coefficient to be eliminated in rows below index best_lead_ind.
Assume that M[row_to_sub] is all zeros before M[row_to_sub][best_lead_ind]
For example, an input might be
M = [[5, 6, 7, 8],
[0,0, 1, 1],
[0, 0, 5, 2],
[0, 0, 7, 0]]
row_to_sub = 1
best_lead_ind = 2
The function should change M to become
M = [[5, 6, 7, 8],
[0, 0, 1, 1],
[0, 0, 0, -3],
[0, 0, 0, -7]]
by adding -5*M[1] to M[2] and -7*M[1] to M[3].
'''


from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def eliminate(M, row_to_sub, best_lead_ind):
    new_matrix = M[:row_to_sub]
    for row in M[row_to_sub+1: ]:
    
        k = solve( (((M[row_to_sub][best_lead_ind])*x)+(M[row][best_lead_ind])), x)
        new_matrix.append(add_rows_coefs(row_to_sub, k, row, 1))
    print_matrix(new_matrix)
    return new_matrix

eliminate([[5, 6, 7, 8],[0,0, 1, 1],[0, 0, 5, 2],[0, 0, 7, 0]], 1, 2)


        
            
            

'''Problem 6.
Write a function with the signature forward_step(M) which takes in an arbitrary matrix M (as a list of
lists), applies the forward step of Gaussian Elimination to it, and modifies M to be the matrix obtained
after the forward step is applied. This can be done by repeatedly calling get_row_to_swap, swapping
rows, and calling eliminate. Unlike with ESC103, I recommend that you keep the entire matrix rather
than extracting submatrices. The process of performing the forward step remains essentially the same.
The process is illustrated on the next page. As you write forward_step(), add print() statements to
forward_step() to produce output similar to the examples provided on this handout (i.e, print out the
matrix transformation process, and comments on what’s happening at every step).'''

def forward_step(M) :
    #identify row to swap as first step, and row we can eliminate easily
        """
    Applies the forward step of Gaussian Elimination to matrix M.
    
    Args:
        M (list of list of floats): The matrix to perform the forward step on.
        
    Modifies M in-place and prints each transformation step.
    """
    n = len(M)  # Number of rows in the matrix
    
    for i in range(n):
        # Get the row to swap with the current row for optimal pivoting, go through all rows and check
        row_to_swap = get_row_to_swap(M, i)
        
        if row_to_swap != i: #if the row i am swapping is not equal to the current row 
            # Swap rows to place the best pivot at the current row
            print(f"Swapping rows {i} and {row_to_swap} for pivot positioning")
            M[i], M[row_to_swap] = M[row_to_swap], M[i]
            print_matrix(M)  # Print the matrix after the swap
            
        # Get the leading index for the current row after swapping
        lead_ind = get_lead_ind(M[i])
    

'''Problem 7.
Write a function with the signature backward_step(M) which takes in an arbitrary matrix M and applies
the backward step of Gaussian Elimination to it. A sample run of the backward step (with automaticallygenerated
explanations of what’s going on) is illustrated at the end of this handout.'''
def forward_step(M):
    n = len(M)  # Number of rows in the matrix
    
    for i in range(n):
        # Get the row to swap with the current row for optimal pivoting
        row_to_swap = get_row_to_swap(M, i)
        
        if row_to_swap != i:  
            # Swap rows to place the best pivot at the current row
            print(f"Swapping rows {i} and {row_to_swap} for pivot positioning")
            M[i], M[row_to_swap] = M[row_to_swap], M[i]
            print_matrix(M)  # Print the matrix after the swap
            
        # Get the leading index for the current row after swapping
        lead_ind = get_lead_ind(M[i])

        if lead_ind == len(M[i]):  # Skip if row is all zeros
            continue  

        # Normalize the pivot row so the leading coefficient is 1
        pivot_value = M[i][lead_ind]
        M[i] = [x / pivot_value for x in M[i]]
        print(f"Normalizing row {i} by dividing by pivot {pivot_value}")
        print_matrix(M)

        # Eliminate rows below
        eliminate(M, i, lead_ind)

    print("Matrix after forward step:")
    print_matrix(M)


'''Problem 8.
Now, write a function that solves the equation Mx = b for the vector x. The idea is to first build the
augmented matrix (M|b), then apply Gaussian Elimination to the augmented matrix, and then solve for
x. Test your solve() function. In numpy.py, we provide code to quickly perform matrix multiplication in
Python so that you can pick arbitrary M and x, obtain a b by multiplying M and x, and then verify that
your algorithm can recover the x'''

def backward_step(M):
    n = len(M)  # Number of rows in the matrix

    for i in range(n - 1, -1, -1):  # Iterate from bottom to top
        lead_ind = get_lead_ind(M[i])  

        if lead_ind == len(M[i]):  # Skip zero rows
            continue

        # Make all elements above the pivot zero
        for j in range(i - 1, -1, -1):
            factor = M[j][lead_ind]
            M[j] = add_rows_coefs(M[j], 1, M[i], -factor)
            print(f"Eliminating element in row {j}, column {lead_ind} using row {i}")
            print_matrix(M)

    print("Matrix after backward step:")
    print_matrix(M)
