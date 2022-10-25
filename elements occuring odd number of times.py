#elements occuring odd number of times

l=eval(input("enter a list"))

for i in l:
    c=0
    c=l.count(i)
    if c%2==1:
        print(i,"is occuring",c,"times")
