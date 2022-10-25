#twin prime number

a=int(input("enter a number"))
b=int(input("enter a number"))
f=0
fb=0
for i in range(1,a+1):
    if(a%i==0):
        f+=1
for i in range(1,b+1):
    if(b%i==0):
        fb+=1
        
    

if(f==2 and fb==2 and (b-a==2)):
    print(a,b,"are twin  prime number")
else:
    print(a,b,"are  not twin  prime number")
    
