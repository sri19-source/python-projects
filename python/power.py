#power of  anumber 
x=int(input("enter a number:"))
y=int(input("enter the power:"))
result=1
while y>0:
    result*=x
    y-=1
print("the result is:", result)