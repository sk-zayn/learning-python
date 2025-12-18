# Object oriented programmin (OOPS)

class Human : #Created class (Human)
  def walk(self):  # wrote function in class human this function can only be used by those who are object of class Human
    print('Walking') #you have to give self as first parameter to the function  in class

  def talk(self):
    print('Talking')

  def eat(self):
    print('Eating')

zain = Human() #zain now became the object of class human and can access all the functions inside human class
zain.walk()
zain.talk()
zain.eat()

class addition:
  def add (self, a, b):
    self.a = a
    self.b = b
    self.c = self.a + self.b
    print(self.c)

add1 = addition()
add1.add(49, 69)

add2 = addition()
add2.add(32, 59)

add4 = addition()
add4.add(48,2)


