#replace the vowel with next alphabet
n=input("enter a string")
x=""

for i in n:
    if i in ("AEIOUaeiou"):
        a=ord(i)      #a= ASCII
        p=chr(a+1)      #next alphabet
        x=x+p
    else:
        x=x+i

print(x)
