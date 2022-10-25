#while loop even digits
n=int(input("enter the number "))

while n!=0:
    d=n%10
    if(d%2==0):
        print(d)
    else:
        print("odd digit")
    n=n//10
