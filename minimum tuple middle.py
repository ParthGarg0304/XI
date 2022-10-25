#middle minimum element

tup=eval(input("enter a tuple: "))
length=len(tup)
lies=False
minimum=min(tup)

if length%2==0:
    half=length//2
    if minimum==tup[half] or minimum==tup[half-1]:
        lies=True

else:
    half=length//2
    if minimum==tup[half]:
        lies==True
        
if lies==True:        
    print("minimum lies in tuple middle")
else:
    print("minimum dosen't lie at tuples middle")
