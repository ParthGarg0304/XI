#pattern 12

n=int(input("enter the number of rows"))
for i in range(n):
    for sp in range(n,i,-1):
        print(" ",end="")
    for j in range(0,i+1):
        if j==0 or j==i:
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()

for e in range(1,(n*2)-2):
    print("*",end=" ")
