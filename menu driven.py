#menu driven
ans='y'
while ans=='y' or ans=='Y':
    print("enter 1 for unique number")
    print("enter 2 for sum-product number")
    ch=int(input("enter choice"))
    if ch==1:
        n=int(input("enter a number"))
        for i in range (0,10):
            k=0
            while n!=0:
                d=n%10
                if d==i:
                    k=k+1
                n=n//10
        if k>1:
            print("is a unique number")
        else:
            print("is not a unique number")          
    elif ch==2:
        n=int(input("enter a number"))
        p=1
        s=0
        while n!=0:
            d=n%10
            p=p*d
            s=s+d
            n=n//10
        if(s==p):
            print("is a sum-product number")
        else:
            print("is not a sum-product number")
    else:
        print("incorrect option")
    ans=input("do you want to proceed(y/n)")
    

