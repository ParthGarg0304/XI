#while loop reverse number
n=int(input("enter a number"))

while n!=0:
    d=n%10
    print(d,end="")
    n=n//10
