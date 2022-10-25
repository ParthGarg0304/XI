#odd numbers
l=eval(input("enter a numerical list"))

for i in range(0,len(l)):
        if l[i]%2==1:
            l[i]=2*l[i]

print(l)
   
