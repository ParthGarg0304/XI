#palindrome and convertion
n=int(input("enter a number"))
num=n
rev=0
f=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
    f=f+1

if(num==rev):
    print(num,"is a palindrome number")
else:
    print(num,"is a not palindrome number")
    nnum=num*(10**f)+rev
    print(nnum,"is the number after conversion")
    print(nnum,"is a palindrome number")
    
