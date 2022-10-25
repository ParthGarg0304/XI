#searching element
lst=[]    #list created  
n=int(input("how many students "))
for i in range(1,n+1):
    name=input("enter the name of students "+str(i)+";")
    lst.append(name)
ntuple=tuple(lst)   #tuple created
name=input("enter name to be searched for")
if name in ntuple:
    print(name,"exists in the tuple")
else:
    print(name,"does not exists in the tuple")

