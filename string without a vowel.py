#a string without vowel
n=input("enter a string")
x=""

for i in n:
    if i in ("AEIOUaeiou"):
        x=x+""
    else:
        x=x+i

print(x)
