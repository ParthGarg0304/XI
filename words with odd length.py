#WORDS WITH ODD LENGTH

l=eval(input("enter a list of words"))
word=[]

for i in l:
    word=i
    if len(word)%2==1:
        print(word)
    

