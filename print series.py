#print series 0,3,8,15,14...
n=int(input("enter the number of terms"))
p=0
d=0
for i in range(1,n+1):
    p=i*i
    d=p-1
    print(d,end=",")
    
    

    
