# sum of series 2-4+6-8...

n=int(input("enter a number"))
s=0
t=2
for i in range(1,n+1):
    if i%2==0:
        s=s-t
    else:
        s=s+t
    t=t+2
print("sum=",s)
    
