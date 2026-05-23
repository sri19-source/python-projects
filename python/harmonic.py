#Compute series: 1 + 1/2 + 1/3 + … + 1/N.
n=int(input("enter the number of terms:"))
sum=0
for i in range(1,n+1):
    sum=sum+1/i
print("the sum of the series is:",sum)