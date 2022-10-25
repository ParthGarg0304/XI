# circular prime number

n=int(input("enter a number"))
num=n
f=0
l=0
i=0
while num>0:
    f=0
    l=l+1
    for i in range(1,n+1):
        if(n%i==0):
            f+=1
    if(f==2):
        d=n%10
        n=n//10
        n=n*10+d
        print("the number after rotating is",n)
        num=n
        i=i+1
    else:
        print(num,"is not a circular prime number")
        break

if(l==i):
    print(num,"is a circular prime number")
