#Python problem-solving labs


"""
Warmup 1 - element_99(L)
Iterates through a list of lists.
Finds and prints the course number associated with the score 99.
Returns the course number if found.
"""
def element_99(L):
    for i in L:
        if i[1] == 99:
            print(i[0])
            return i[0]
    
"""
Warmup 2 - get_nums(L)
Extracts all numerical values (scores) from the given list.
Stores them in a new list and prints the result.
"""

def get_nums(L):
    new_L = []
    for i in L:
        new_L.append(i[1])
    print(new_L)

"""
Warmup 3 - lookup(L, num)
Searches for a specific score in the list.
Returns the corresponding course number if found.
Returns None if the score is not in the list.
"""

def lookup(L, num):
    for i in L:
        if i[1] == num:
            print(i[0])
            return i[0]


''' Problem 4 '''

"""
Problem 4 - Energy Computation - hopfield networks 
    E(x0, x1, x2, w01, w02, w12)
    Computes the energy function for a set of binary inputs (-1 or 1).
    Uses weighted pairwise interactions between x0, x1, and x2.
    Returns the negative sum of these interactions.
    print_all_energies(w01, w02, w12)
    Iterates through all possible (-1,1) combinations of x0, x1, and x2.
    Computes energy values for each combination.
    Prints the input values and corresponding energy.

Problem 4 - Weight Adjustment & Iterative Learning
    adjust_weights(x, y, z)
        Adjusts the weights (w01, w02, w12) based on input values.
        Increases the weight by 0.1 if two inputs have the same sign.
        Decreases the weight by 0.1 if the inputs have opposite signs.
        Returns the updated weights.
    repeat_adjust(n)
        Runs adjust_weights() n times.
        Prints the adjusted weights after each iteration.
        Calls print_all_energies() to display the energy transformation process.
Final Execution in __main__
    Initializes the weights (w01, w02, w12).
    Calls print_all_energies() to compute initial energy values.
    Calls repeat_adjust(4) to adjust weights over 4 iterations and track changes.
"""

def E(x0, x1, x2, w01, w02, w12):
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    return -(term1 + term2 + term3)

def print_all_energies(w01, w02, w12):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
            
                print("x: (", x0, x1, x2, ")", "E:", E(x0, x1, x2, w01, w02, w12))
                       
if __name__ == '__main__':
    w01 = 2
    w02 = -1
    w12 = 1
    print_all_energies(w01, w02, w12)
       
def adjust_weights(x,y,z):
        x0 = x
        x1 = y
        x2 = z
        global w01, w02, w12
        if x0*x1>0:
            w01+=0.1
        else:
            w01-=0.1
            
        if x0*x2>0:
            w02+=0.1
        else:
            w02-=0.1
        if x1*x2>0:
            w12+=0.1
        else:
            w12-=0.1
        return w01, w02, w12
    
def repeat_adjust(n):
    for i in range(0,n):
        print("adjusted ; ")
        global x,y,z
        adjust_weights(x,y,z)
        print_all_energies(w01, w02, w12)
        #store it
              
if __name__ == '__main__':
    x,y,z = -1,1,1
    repeat_adjust(4)
    


        
        

