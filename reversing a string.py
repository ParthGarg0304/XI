#reversing a string
n=input("enter a string")
ctr=n
x=""

for i in range(len(str)-1,-1,-1):
    x=x+n[i]
print("reverse is::",x)
