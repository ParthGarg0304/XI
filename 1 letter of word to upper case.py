#1st letter of each word to uppercase
n=input("enter a sentence")
n=n+" "
x=""
a=""
for i in n:
    if i!=" ":
        x=x+i
    else:
        if x[0] in ("QWERTYUIOPLKJHGFDSAZXCVBNM"):
            print(x,end=" ")           
        else:
            f=x[0]           #to extract first letter
            a=a+f.upper()
            print(x.replace(x[0],a),end=" ")
        x=""
        a=""
            
