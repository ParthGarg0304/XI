#HARSHAD number

n=int(input("enter a number"))
num=n
f=0
h=0    #h and f to check if no of timesloop executed =no of times if true
while n>=10:
    s=0
    f=f+1
    while n!=0:
        d=n%10
        s=s+d
        n=n//10
    if(num%s==0):
        num=num/s
        n=num
        h=h+1
    else:
        break

if(h==f):
    print("a harshad number")
else:
     print("not a harshad number")
