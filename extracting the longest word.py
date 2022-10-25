#longest word
n=input("enter a sentence")
n=n+" "
x=""
longest=""
max=0
for i in n:
    if i!=" ":
        x=x+i
    else:
        l=len(x)
        if l>max:
            max=l
            longest=x
        x=""
print(longest)

