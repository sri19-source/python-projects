#count how many digits are even in a number
n=int(input("enter the number:"))
count=0
for i in str(n):
    if int(i)%2==0:
        count=count+1
print("the number of even digits in the number is:",count)