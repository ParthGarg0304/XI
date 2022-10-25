#List of strings with first characters removed
l=eval(input("Enter a list of words::"))
for i in range(len(l)):
    l[i]=l[i][1:]
    print(l[i],end=" ")
    
