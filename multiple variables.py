x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
# Multiple variables can be assigned in one line

x=y=z=w= "Orange"
print(x)
print(y)
print(z)
print(w)
# One value to multiple variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# Unpack a collection
# If the number of variables is less than the number of values, you can use an asterisk to collect the remaining values as a list.


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
x, y, *z = fruits
print(x)        
print(y)
print(z)
# Assign the rest of the values as a list

fruits = ["apple", "banana"]
x, y, *z = fruits
print(x)
print(y)
print(z)
# If the number of variables is more than the number of values, Python will raise an error.