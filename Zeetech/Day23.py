class employee :
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary
    print(self.name, self.age, self.salary)

emp1 = employee("John", 30, 50000)
emp2 = employee("Alice", 28, 60000)



# inheritence
# it means child class will have parent calss feature as well as it own features
# inheritence supports code reusability

class Rehman:
  def polite(self):
    print('he is a polite person')

class ayaz (Rehman): # passing class in another class make the class in which the other class is pass child class
  def graduate (self):
    print('Yes he is graduate')

obj1 = ayaz()
obj1.graduate()
obj1.polite()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student(Person):
  def __init__(self, name, age, roll_no, course):
    self.roll_no = roll_no
    self.course = course
    super().__init__(name, age)
    print(self.name, self.age, self.roll_no, self.course)

obj2 = Student('zain', 22, 1, 'web development')

class teamLeader:
  def __init__(self, name, exp):
    self.name = name
    self.exp = exp

class teamMembers:
  def __init__(self, sal, designation):
    self.sal = sal
    self.designation = designation

class Worker(teamLeader, teamMembers):
  def __init__(self, name, exp, sal, designation, address):
    teamLeader.__init__(self, name, exp)
    teamMembers.__init__(self, sal, designation)
    self.address = address
    print(self.name, self.exp, self.sal, self.designation, self.address)


obj4 = Worker('zain', 2, 20000, 'developer', 'mumbra')


l1 = [1, 2, 3, 4, 5]
sum = 0
for i in l1:
  sum += i

print(sum)


str = 'String'
print(str[::-1])


dictionary = {
  'name' : 'zain',
  'age' : 22,
  'address' : 'mumbra'
}

for i, j in dictionary.items():
  print(i, j)

strinput = input('Enter a string here: ')
char = {}

for i in strinput:
    if i != ' ':
        if i not in char:
            char[i] = 1
        else:
            char[i] += 1

print(char)

