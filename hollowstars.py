n=int(input("length: "))
m=int(input("height: "))
starstr=n*"*"
print(starstr)
hollows=m-2
for number in range(0,hollows):
    space=int(n-2)
    hollowstr=str(("*")+(" "*space)+("*"))
    print(hollowstr)
print(starstr)
 