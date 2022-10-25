#grades

marks=eval(input("enter marks in 5 subject"))
total=sum(marks)
avg=total/5

if avg>=75:
    grade='A'

elif avg>=60:
    grade='B'

elif avg>=50:
    grade='c'

else:
    grade='D'

print("total marks:",total,"grade: ",grade)
    
