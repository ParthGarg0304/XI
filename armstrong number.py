#armstrong number
n=int(input("enter a number"))
num=n
n2=n
s=0
s2=0

while n!=0:
    d=n%10
    s=s+1
    n=n//10
    
while n2!=0:
    d=n2%10
    s2=s2+d**s
    n2=n2//10    

if(s2==num):
    print(num,"is a armstrong number")
else:
     print(num,"is not a armstrong number")

