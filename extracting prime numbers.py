#prime numbers
l=eval(input("enter a numerical list"))
k=0
for i in l:
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k+=1

    if k==2:
        print(i)
