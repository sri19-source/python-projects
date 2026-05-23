x="3"
y="2" 
print(x*int(y))  # This will raise an error because you cannot add int and str directly
z=int(y)
print(z)

nums=[10,20,30]
nums[1]=""
print(nums)

x=[1,2,3]
x=x+[4]
print(x)  # This will work because you are concatenating a list with another list

n=1
while n<5:
    n+=1
    print(n)  # This will print numbers from 2 to 5
     

a=10
b=20
a,b=b,a
print(a, b)  # This will print 20 10, demonstrating tuple unpacking for swapping values