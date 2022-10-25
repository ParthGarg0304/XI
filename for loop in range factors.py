# for loop for  even factor
n=int(input("enter a number"))
ctr=0
for i in range(1,n+1):
    if(n%i==0 and i%2==00):
        print("even factor=",i)
        ctr+=1

if ctr==0:
    print("no even factors")
        
