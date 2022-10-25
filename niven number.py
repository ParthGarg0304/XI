#niven  number
n=int(input("enter a number"))
num=n
s=0

while n!=0:
    d=n%10
    s=s+d
    n=n//10

if(num%s==0):
    print(num,"is a niven number")
else:
     print(num,"is not a niven number")

