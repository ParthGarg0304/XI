# type of triangle
a=int(input("enter a side of triangle"))
b=int(input("enter a side of triangle"))
c=int(input("enter a side of triangle"))

if(a+b>c and a+c>b and b+c>a):
    print("triangle possible")
    if(a==b and b==c and c==a):
        print("equilateral triangle")

    elif(b==a or b==c or c==a):
        print("isocelous triangle")

    else:
        print("scalance triangle")
        
else:
    print("triangle not possible")
   
