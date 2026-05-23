"""`s = "Python"
print(s[-4:-1])
    """
"""x = 5
print(x > 3 and x < 5 or x == 5)"""
"""for i in range(2):
    for j in range(2):
        if i == j:
            break
        print(i, j)"""
"""i = 1
while i < 5:
    print(i)
    if i == 3:
        continue
    i += 1"""
"""t = (1, 2, 3)
t[0] = 10
"""
""" f = open("test.txt", "w")
f.write("Hello")
f.read()"""
"""def func(x):
    if x < 0:
        raise ValueError("Negative")
    return x

print(func(-1))"""
"""lst = [10, 20, 30]
print(lst.index(40))"""
"""k=1,2,3
print(type(k)) """
"""with open("sample.txt", "w") as f:
          f.write("Hello")
with open("sample.txt", "r") as f:
           c=f.read() 
           print(c)"""
"""import urllib.request
data=urllib.request.urlopen("http://practicle.com")
print(data.status)"""
"""x = (1,2,3)
x[0] = 5
print(x)"""
class Badge:
    def __init__(self, val):
        self.val = val

b = Badge(1)
d = {b: 'Active'}
b.val = 2
print(d.get(b))