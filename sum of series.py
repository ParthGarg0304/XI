#sum of series 1/2+2/3+3/4...
n=int(input("enter the number of terms"))
s=0

for i in range(1,n+1):
    s=s+i/(i+1)

print("sum=",s)
