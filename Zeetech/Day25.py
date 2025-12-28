# method overloading happens when two or more function are there with same name, same data type and same count of variable
from multipledispatch import dispatch

class addition:
  @dispatch(int, int)
  def add (self, x, y):
    z = x + y
    print(z)

  @dispatch(int, int, int)
  def add (self, x, y, z):
    a = x + y + z
    print(a)

  @dispatch(float, float)
  def add (self, x, y):
    z = x + y
    print(z)

a = addition()
a.add(10, 20)
a.add(10, 20, 30)
a.add(10.5, 20.5)


class vehicle:
  def run (self):
    print('vehicle is running')

class bike(vehicle):
  def run (self):
    print('bike is running')

class car(vehicle):
  def run (self):
    print('car is running')

lambo = car()
lambo.run()


# Write a function to find common elements between two lists.

l1 = [1, 2, 3, 4, 5, 6]
l2 = [5, 6, 7, 8, 9, 2]

l3 = []
def commonNumber(l1, l2):
  for i in l1:
    if i in l2 :
      l3.append(i)
  return(l3)

print(commonNumber(l1, l2))


