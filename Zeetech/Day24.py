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


# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_person(self):
#     print(self.name)
#     print(self.age)

# class employee:
#   def __init__(self, id, sal):
#     self.id = id
#     self.sal = sal

#   def show_employee(self):
#     print(self.id)
#     print(self.sal)

# class Manage(person, employee):
#   def __init__(self, name, age, id, sal, designation):
#     self.desig = designation
#     self.show_person()
#     self.show_employee()


class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_person(self):
    print(self.name, self.age)

class employee(person):
  def __init__(self, name, age, id, sal):
    self.id = id
    self.sal = sal
    super().__init__(name, age)

  def show_employee(self):
    self.show_person()
    print(self.id, self.sal)

class manager(employee):
  def __init__(self, name, age, id, sal, dept):
    self.dept = dept
    super().__init__(name, age, id, sal)

  def show_manager(self):
    self.show_employee()
    print(self.dept)

m = manager('zain', 22, 1, 200000, 'it')
m.show_manager()
