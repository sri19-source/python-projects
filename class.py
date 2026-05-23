class Myclass:
    x=5
p1 = Myclass()
print(p1.x)
print(Myclass)

#__init__
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("Gwen", 17)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

