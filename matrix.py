"""
This program performs matrix addition on two 2D lists (matrices) if they have matching dimensions.

It first checks if the number of rows and columns in both matrices are equal.
If the dimensions match, it creates a new matrix where each element is the sum of corresponding elements from matrices A and B.
If the matrices do not have the same dimensions, the function returns nothing.
The sum matrix is both returned and printed.
This function is useful in linear algebra computations, where matrix operations are needed for data analysis, graphics transformations, and scientific calculations.
"""

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
