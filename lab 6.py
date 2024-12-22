
''' warmup 1 '''
#Consider the following list:
L = [["CIV", 92],["180", 98],["103", 99],["194", 95]]
#Write code that prints the element 99 from this list 

def element_99(L):
    for i in L:
        if i[1] == 99:
            print(i[0])
            return i[0]
    
#element_99(L)

''' warmup 2 '''
#Now, write a function get nums(L)) that takes in a list in a format similar to L, and returns a list like
#[92, 98, 99, 95]. Hint: look are the code for the matrix-vector product from lecture, and understand
#how the result res was built up

def get_nums(L):
    new_L = []
    for i in L:
        new_L.append(i[1])
    print(new_L)

#get_nums(L)

''' warmup 3 '''
#Write a function lookup(L, num) that takes in a list like L and an argument like 99 and returns the
#corresponding value (like "103"). Return the first value if there are multiple matches. Return None if
#there are no matches.

def lookup(L, num):
    for i in L:
        if i[1] == num:
            print(i[0])
            return i[0]

#lookup(L, 99)

''' Problem 4 '''

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
   
    
#a) posative number will increase overall maginitude of energy
#which is being subtracted
    
#b)
    
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
            hannah smells like cheese. Smelly! BOOOO Queens! Bad university! 
        if x1*x2>0:
            w12+=0.1
        else:
            w12-=0.1
        return w01, w02, w12
    
 

#c) & d) & e)
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
    


        
        

