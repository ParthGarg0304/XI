# automorphic number
n=int(input("enter a number"))
sq=n*n
num=n
x=0
while n!=0:
    d=n%10
    x=x+1
    n=n//10

import math
rem=sq%math.pow(10,x)
if(rem==num):
    print(num,"is a automorphic number")
else:
     print(num,"is not  a automorphic number")


