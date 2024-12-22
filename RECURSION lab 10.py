# Problem 1: Recursive Power Function

# Part (a)
# To decompose x^n into smaller problems, we can use x * x^(n-1) as the recursive step.
# The base case is when n == 0, where x^0 is 1. This is the simplest subproblem.
# The recursive step is multiplying x by power(x, n - 1) until n reaches 0.

# Part (b)
def power(x, n):
    """
    Computes x raised to the power of n recursively using only multiplication.
    
    Parameters:
    x (int or float): The base value.
    n (int): The exponent value (non-negative).
    
    Returns:
    int or float: The result of x raised to the power n.
    
    Example:
    power(2, 3) returns 8.
    """
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive step: multiply x by the result of power(x, n-1)
    else:
        return x * power(x, n - 1)

# Example usage
print(power(2, 3))  # Output: 8

# Part (c)
# Call tree for power(2, 3):
# power(2, 3)
#     └── 2 * power(2, 2)
#             └── 2 * power(2, 1)
#                     └── 2 * power(2, 0)
#                             └── 1
# Result: 2 * 2 * 2 * 1 = 8

# Problem 2: Sum of Digits Function

# Part (a)
# The base case for summing the digits of a number is when the number has only one digit (i.e., n < 10).
# In that case, we can return the digit itself.
# The recursive step is to extract the last digit using n % 10, and add it to the result of sum_digits(n // 10).

def sum_digits(n):
    """
    Sums up the digits of a given number recursively.
    
    Parameters:
    n (int): The number whose digits are to be summed (must be non-negative).
    
    Returns:
    int: The sum of the digits of n.
    
    Example:
    sum_digits(123) returns 6.
    """
    # Base case: if n is a single digit, return n
    if n < 10:
        return n
    # Recursive step: add the last digit to the sum of the rest of the digits
    else:
        return n % 10 + sum_digits(n // 10)

# Example usage
print(sum_digits(123))  # Output: 6

# Problem 3: Split List into Sublists

# Part (a)
# Write a helper function that splits a list into sublists separated by a single element.
# This function will help divide the list whenever it encounters the specified separator element.

def split_by_element(lst, separator):
    """
    Splits a list into sublists separated by a given element.
    
    Parameters:
    lst (list): The list to be split.
    separator (any type): The element used as the separator.
    
    Returns:
    list of lists: The resulting list of sublists.
    
    Example:
    split_by_element([1, 2, 3, 4], 3) returns [[1, 2], [4]].
    """
    sublists = []
    current_sublist = []
    
    for elem in lst:
        if elem == separator:
            if current_sublist:
                sublists.append(current_sublist)
                current_sublist = []
        else:
            current_sublist.append(elem)
    
    if current_sublist:
        sublists.append(current_sublist)
    
    return sublists

# Part (b)
# Use the helper function to split a list by multiple elements.
# Iterate through all separators and use the helper function to split the list repeatedly.

def split_by_multiple_elements(lst, separators):
    """
    Splits a list into sublists separated by any of the given elements.
    
    Parameters:
    lst (list): The list to be split.
    separators (list): The list of elements used as separators.
    
    Returns:
    list of lists: The resulting list of sublists.
    
    Example:
    split_by_multiple_elements([1, 2, 6, 4, 5, 3, 7], [3, 6]) returns [[1, 2], [4, 5], [7]].
    """
    result = lst
    for separator in separators:
        # Split the list by the current separator
        temp_result = []
        for sublist in result:
            temp_result.extend(split_by_element(sublist, separator))
        result = temp_result
    
    return result

# Example usage
print(split_by_multiple_elements([1, 2, 6, 4, 5, 3, 7], [3, 6]))  # Output: [[1, 2], [4, 5], [7]]
