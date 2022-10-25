#word with maximum vowels

l=eval(input("enter a list of words"))
maxi=0
maxw=[]

for i in l:
    count=0
    for j in range(0,len(i)):
        if i[j]=='a' or i[j]=='e' or i[j]=='i' or i[j]=='o' or i[j]=='u' :
            count+=1
    if count>maxi:
        maxi=count
        maxw.clear()
        maxw=i
    elif maxi==count:
        maxi=count
        maxw+=','+i

print(maxw)

        


    
