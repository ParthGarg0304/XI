# co primes
a=int(input("enter a number"))
b=int(input("enter a number"))

for i in range(1,a+1):
    if a%i==0 and b%i==0:
        h=i

if(h==1):
    print(a,b,"are co prime",sep="  ")
else:
    print(a,b,"are not co prime",sep="  ")
    
