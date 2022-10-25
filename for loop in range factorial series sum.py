#sum of series 1!+2!+3!+4!...
a=int(input("enter a number of terms"))
s=0
for i in range(1,a+1):
    f=1
    for j in range(1,a+1):
        f=f*j
    s=s+f
    
print("factorial series sum =",s)

