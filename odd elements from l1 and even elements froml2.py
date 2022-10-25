#odd elements from l1 and even elements froml2
l1=eval(input("enter a numerical list"))
l2=eval(input("enter a numerical list"))
l3=[]

for i in l1:
    if i%2==1:
        l3.insert(len(l1),i)
            
for i in l2:
    if i%2==0:
        l3.insert(len(l2),i)
            

print(l3)
   
