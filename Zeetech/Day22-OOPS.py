# Object oriented programmin (OOPS)

class Human : #Created class (Human)
  def walk():  # wrote function in class human this function can only be used by those who are object of class Human
    print('Walking')

  def talk():
    print('Talking')

  def eat():
    print('Eating')

zain = Human() #zain now became the object of class human and can access all the functions
zain.walk()
zain.talk()
zain.eat()

