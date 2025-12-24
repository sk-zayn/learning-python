# This is an example of multilevel inheritence
class grandfathet:
  def grandfather(self):
    print('I am the grandfather')

class father(grandfathet):
  def father(self):
    print('I am the father')

class son(father):
  def son(self):
    print('I am the son')

obj1 = son()
obj1.grandfather()
obj1.father()
obj1.son()

obj2 = father()
obj2.father()
obj2.grandfather()

