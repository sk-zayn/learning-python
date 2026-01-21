from random import *
class Dice:
  def __init__(self, sides = 6):
    self.sides = sides

  def roll_dice(self):
    return randint(1, self.sides)


d = Dice()
print(d.roll_dice())
print(d.roll_dice())



