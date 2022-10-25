#even digits
n=int(input("enter a number"))

num=0
while n!=0:
    d=n%10
    if(d%2==1):
        num=num*10+d
    n=n//10
    
while num!=0:
    d=num%10
    print(d,end="")
    num=num//10


