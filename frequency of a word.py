#frequency of a word in a sentence
n=input("enter a sentence")
word=input("enter the word to be searched")
ctr=0
n=n+" "
x=""
for i in n:
    if i!=" ":
        x=x+i
    else:
        if x==word:
            ctr+=1
        x=""

print(word,"occured",ctr,"times")
