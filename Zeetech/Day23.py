class employee :
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary
    print(self.name, self.age, self.salary)

emp1 = employee("John", 30, 50000)
emp2 = employee("Alice", 28, 60000)
