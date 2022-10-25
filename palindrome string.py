#palindrome string
n=input("enter a string")
ctr=n
x=""

for i in range(len(n)-1,-1,-1):
    x=x+n[i]
print("reverse is::",x)

if x==ctr:
    print("it is a palindrome string")
else:
    print("it is not a palindrome string")
    
