#palindrome
n=int(input("enter a number"))
num=n
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10

if(num==rev):
    print(num,"is a palindrome number")
else:
    print(num,"is a not palindrome number")
    
