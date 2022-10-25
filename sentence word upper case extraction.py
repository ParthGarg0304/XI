#Displaying words starting with uppercase
n=input("Enter a sentence::")
n=n+' '
x=""
for i in range(len(n)):
    if n[i]!=" ":
        x=x+n[i]
        
    else:
        if ord(x[0])>=65 and ord(x[0])<=90:
            print(x)
        x=""
