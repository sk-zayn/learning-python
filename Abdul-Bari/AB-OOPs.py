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
    super().__init__(l, b) #Super is used to call the constructor of the parent class

c = cuboid(10, 5, 3) # we have to pass all the parameters here including the parent class parameter

print('volume of cuboid is ', c.volume())


