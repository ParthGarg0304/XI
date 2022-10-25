#special number
n=int(input("enter a number"))
num=n
f=1
s=0

while n!=0:
    d=n%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    n=n//10

if(s==num):
    print(num,"is a special number")
else:
     print(num,"is not a special number")

