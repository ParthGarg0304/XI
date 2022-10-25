#fibonocci series
n=int(input("enter a number of terms"))
a,b,c=0,1,0
print(a,",",b,",",end="")
for i in range(n-3):
    c=a+b
    print(c,",",end=" ")
    a=b
    b=c
    
c=a+b
print(c)

