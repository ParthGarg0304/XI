a=int(input("enter a number"))
b=int(input("enter a number"))

for i in range(a+1):
    if(a%i==0 and b%i==0):
        h=i
lcm=(a*b)//h

print("hcf=",h)
print("lcm",lcm)
    
