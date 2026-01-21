class Cuboid:
  def __init__(self, length, breadth, height):
    self.l = length
    self.b = breadth
    self.h = height

  def lidArea(self):
    return self.l * self.b

  def volume(self):
    return self.l * self.b * self.h

  def total(self):
    return 2*(self.l * self.b + self.b * self.h + self.h * self.l)


c1 = Cuboid(10, 5, 3)
print(c1.volume())

c2 = Cuboid(20, 10, 5)
print(c2.volume())


class rectangle:
  def __init__(self, l, b):
    self.length = l
    self.breadth = b

  def area(self):
    return self.length * self.breadth

  def volume(self):
    return 2 * (self.length + self.breadth)

class cuboid(rectangle):
  def __init__(self, l, b, h):
    self.height = h
    self.length = l #either you can re initialize the parameter in the child calss of use super like below
    self.breadth = b
    # super().__init__(l, b) #Super is used to call the constructor of the parent class

c = cuboid(10, 5, 3) # we have to pass all the parameters here including the parent class parameter

print('volume of cuboid is ', c.volume())





#Polymorphism
#when you write 2 functions with same name the last one will count
class Arith:
  def sum(self, x, y):
    return x + y

  def sum(self, x, y, z):
    return x + y + z

a = Arith()
# print(a.sum(10, 65))
#now you wont be able to pass just two parameters cause the last sum function takes 3 parametters


#with this method you can call sum function with  2 and 3 parameters and it wont give error this is called method overloading
class Aritimetic:
  def sum (self, x, y, z=None):
    s = x + y
    if z == None:
      return s
    else:
      return x + y + z

s = Aritimetic()
print(s.sum(23, 7))
print(s.sum(23, 7, 5))



class Rational:

  def __init__(self, p = 1, q =1):
    self.p = p
    self.q = q

  def __add__(self, other):
    s = Rational()
    s.p = self.p * other.q + self.q * other.p
    s.q = self.q * other.q
    return s

r1 = Rational(2, 4)
r2 = Rational(2, 5)

sum = r1 + r2
print(sum.p, sum.q)


