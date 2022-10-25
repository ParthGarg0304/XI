# divisiblity using elif

x=int(input("enter a number"))

if(x%5==0) and (x%3==0):
    print("FIZZBUZZ")

elif(x%5==0):
    print("BUZZ")

elif(x%3==0):
    print("FIZZ")

else:
    print("NOT DIVISIBLE")


