#while loop duck number
n=int(input("enter the number of rows"))
num=n
k=0
while n!=0:
    d=n%10
    if(d==0):
        k=k+1
    n=n//10
if(k>=1):
    print(num,"is a duck number")
else:
    print(num,"is not  a duck number")
    
