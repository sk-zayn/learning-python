class NegativAgeException(Exception):
  pass

def stage(age):
  if age < 0 :
    raise NegativAgeException('Age should not be 0 or negative')
  elif age < 13 and age > 0:
    print("Child")
  elif age < 20 and age > 13:
    print("Teen")
  elif age < 40 and age > 20:
    print("Adult")
  elif age > 40:
    print("Senior")

age= int(input("Enter your age: "))
try:
  stage(age)
except NegativAgeException as e:
  print(e)

