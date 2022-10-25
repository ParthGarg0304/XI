# sum of series
n=int(input("enter the number of terms"))
a=2
b=9
s=0

for i in range(1,n+1):
    if i%2==0:
        s=s-(a/b)
    else:
        s=s+(a/b)
    a=a+3
    b=b+4

print(s)

