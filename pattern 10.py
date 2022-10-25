#pattern 9
n=int(input("enter the number of rows"))
for i in range(n+1,0,-1):
    for sp in range(i,n+1,1):
        print(" ",end=" ")
    for j in range(i):
        print("* ",end=" ")
    print()
