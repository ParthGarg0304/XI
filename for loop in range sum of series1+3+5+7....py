# sum of series 1+3+5+7...
a=int(input("enter a number"))
s=0

for i in range(1,(a*2)+1,2): #double n cos due to skip loop execute half times
    s=s+i

print("sum =",s)
