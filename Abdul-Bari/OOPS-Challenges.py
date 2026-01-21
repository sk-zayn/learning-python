from random import *
import math
class Dice:
  def __init__(self, sides = 6):
    self.sides = sides

  def roll_dice(self):
    return randint(1, self.sides)


d = Dice()
print(d.roll_dice())
print(d.roll_dice())


class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    area = math.pi * self.radius * self.radius
    return area

  def parameter(self):
    parameter = 2 * math.pi * self.radius
    return parameter


c = Circle(8)

print(c.area())
print(c.parameter())
print(math.pi)
