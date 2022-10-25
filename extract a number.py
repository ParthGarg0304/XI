# extract a digit
n=int(input("enter a number"))
d=n%10      #to extract digit
n=n//10      #to get the rest number

print(d,n,sep='  ')
