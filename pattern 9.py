#pattern 9
n=int(input("enter the number of rows"))
for i in range(0,n+1):
    for sp in range(n-1,i,-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("* ",end=" ")
    print()
