cp=int(input("enter the cost price"))
sp=int(input("enter the selling price"))

if(sp>cp):
    p=sp-cp
    pp=(p/cp)*100
    print("profit %=",pp)

else:
    l=cp-sp
    lp=(l/cp)*100
    print("loss %=",lp)
    
