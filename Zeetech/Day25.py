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
