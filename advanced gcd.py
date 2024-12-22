import math

pii = 0
n= 1
i=0
while round(pii*4,n) != round((math.pi),n):
    term =((-1)**i)/(2*i+1)
    pii += term
    i+=1

print(pii*4) 