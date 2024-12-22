#If all three sides of a right-angled triangle are integers, the set of these three numbers is known as a
#Pythagorean triple. For example, (3, 4, 5) is a Pythagorean triple because 32+42=52 Write a
#program that displays all Pythagorean triples where the hypotenuse is no larger than 500 units
Pytriple=set()
for a in range(1,501):
    for b in range(1,501):
        for c in range(1,501):
            if ((a**2)+(b**2)==(c**2)):
                Pytriple.add((a,b,c))
                print(Pytriple)
                Pytriple=set()
            else:
                continue