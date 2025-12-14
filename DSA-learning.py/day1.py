# print('Hello, World!')
# a, b, c, d, e = 10, 30.4, 'zain', True, 34+6j
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# num1 = int(input('Enter a number here: '))
# num2 = int(input('Enter a number here: '))
# print(num1 + num2, num1 - num2)

# year = int(input('Enter year here: '))
# if year % 4 == 0 and year % 100 != 0:
#   print('Its a leap year')
# elif year % 400 == 0:
#   print('Its a leap year')
# else:
#   print('Its not a leap year')

num1 = int(input('Enter a number here: '))
num3 = input('Enter the operator you want to perform on numbers: ')
num2 = int(input('Enter a number here: '))

if num3 == '*':
  print(num1 * num2)
elif num3 == '+':
  print(num1 + num2)
elif num3 == '-':
  print(num1 - num2)
elif num3 == '/':
  print(num1 / num2)

celciusOrFerenhite = input ('For celcius write c for ferenhite write f')

if celciusOrFerenhite.lower() == 'c':
  temperature = float(input('Enter you temperature: '))
  tempconvert = temperature * 1.8 + 32
  print(tempconvert)
elif celciusOrFerenhite.lower() == 'f':
  temperature = float(input('Enter you temperature: '))
  tempconvert = (temperature - 32) / 1.8
  print(tempconvert)
else:
  print('You have to enter c  or f ')







