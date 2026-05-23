x="is awesome"
def myfunc():
     print("python " + x)

myfunc()

# This code defines a global variable `x` and a function `myfunc` that prints a message using the global variable.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)