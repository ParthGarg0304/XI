#Frequency of each letter in a string
n=input("Enter a sentence::")
ctr=0
x=""
for i in n:
    if i not in x and i!=' ':
        x=x+i
for i in x:
    for j in n:
        if i==j:
            ctr+=1
    print(i,"=",ctr,"times")
    ctr=0
