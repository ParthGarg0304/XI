# magic number
n=int(input("enter a number"))
num=n
s=n
while s>9:
    n=s
    s=0
    while(n!=0):
        d=n%10
        s=s+d
        n=n//10

if(s==1):
    print(num,"is a magic number")

else:
    print(num,"is not a magic number")
      
        

