#fibonacci series
n=int(input("enter the number of terms:"))
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
print('the fibonacci series is:')
while n>0:
    print(x)
    t=x+y
    x=y
    y=t
    n-=1

 
