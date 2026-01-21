from random import *
import math
#Question 1
class Dice:
  def __init__(self, sides = 6):
    self.sides = sides

  def roll_dice(self):
    return randint(1, self.sides)


d = Dice()
print(d.roll_dice())
print(d.roll_dice())


#Question 2
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


#Question 3
class Book:
  def __init__(self, title, author, price):
    self.title = title
    self.author = author
    self.price = price

  def show_details(self):
    print('Title:', self.title)
    print('Author:', self.author)
    print('Price:', self.price)


b = Book('The Alchemist', 'Paulo Coelho', 1200)

b.show_details()


#Question 4
class Employee:
  emp_count = 101
  def __init__(self, name, designation, salary):
    self.name = name
    self.designation = designation
    self.salary = salary
    self.eid = 'e' + str(Employee.emp_count)
    Employee.emp_count += 1

  def show_details(self):
    print('Name :', self.name)
    print('Eid :', self.eid)
    print('Designation :', self.designation)
    print('Salary :', self.salary)
    print('')

  @classmethod
  def total_emp_count(cls):
    print(cls.emp_count - 101)

e1 = Employee('zaid', 'developer', 80000)
e2 = Employee('zain', 'engineer', 50000)
e3 = Employee('zainab', 'ui-ux', 30000)

e1.show_details()
e2.show_details()
e3.show_details()

print(e1.total_emp_count())


#Question 5
class Calculator:
  @staticmethod
  def add (a, b):
    return a + b

  @staticmethod
  def sub (a, b):
    return a - b

  @staticmethod
  def mul (a, b):
    return a * b

  @staticmethod
  def div (a, b):
    return a / b

x = 10
y = 3

print(Calculator.add(x, y))
print(Calculator.sub(x, y))
print(Calculator.mul(x, y))


#Question 6
class Customer:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone

  def get_name (self):
    return self.name

  def get_phone (self):
    return self.phone

  def set_phone (self, phone):
    self.phone = phone

c = Customer('zaid', '9876543210')
print(c.get_name())
print(c.get_phone())

c.set_phone('1234567890')
print('')
print(c.get_name())
print(c.get_phone())

