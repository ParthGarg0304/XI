#multiple maximum elements

tup=eval(input("enter a tuple: "))
maximum=max(tup)
if tup.count(maximum)>1:
    print("contains maximum multiple elements")
else:
    print("contains only one maximum elements")
