import math

#check if a number is square
def is_square_number(n):
    if math.sqrt(n)//1==0:
        return True
    else:
        return False

#radical to simple
def simplify_radical(r):

    if is_square_number(r):
        a = int(r ** 0.5)
        b = 1
    else:
        a = 1
        b = r
        for i in range(2, int(r ** 0.5) + 1):
            if r % (i ** 2) == 0:
                a *= i
                b = r // (i ** 2)
    return (a, b)

#simple to radical
def print_radical(a, b):
    if a == 1:
        print("\u221A", b)
        return
    else:
        print(f"{a}\u221A{b}")
        return

