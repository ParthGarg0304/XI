#maximum and minimum digits
n=int(input("enter a number"))
mini=9
maxi=0


while n!=0:
    d=n%10
    if(d>maxi):
        maxi=d
    if(d<mini):
        mini=d
    n=n//10
    



print(maxi,"is maximum number")
print(mini,"is minimum number")

