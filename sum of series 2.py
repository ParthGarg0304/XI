#sum of series 1+x**2+x**3+...
x=int(input("enter the base"))
n=int(input("enter the number of terms"))

s=1
for i in range(2,n+1):
    p=x**i
    s=s+p

print(p)
