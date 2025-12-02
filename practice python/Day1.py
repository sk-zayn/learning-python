# 1. Create variables name, age, and height and print them using one print statement.
name = 'zain'
age = 22
height = 5.10
print(name, age, height)

# 2. Store two numbers and print their addition, subtraction, multiplication, and division.
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

# Take user input for a number and print whether it is an integer or a float.
num = input('Enter a number here ')
if '.' in num :
  print('Its a float')
else:
  print('Its an integer')

# Swap two variables without using a third variable.
a = 20
b = 3

temp = a 
a = b 
b = temp

print(a)
print(b)

# Write a program to calculate the area of a rectangle (length × width).
len = 30 
breadth = 5
area = len * breadth
print(area)

# Take a number from the user and print its square and cube.
num = int (input('Enter a number here '))
print(num * num)
print(num * num * num)

# Convert temperature from Celsius to Fahrenheit.
C = int(input('Enter the temperature in C here '))
F = (9/5 * C) + 32
print(F)


# Take a number and check if it is even or odd.
num = int(input('Enter a number here: '))
if num % 2 == 0:
  print('Even')
else:
  print('Odd')

# Check if a person is eligible to vote (age ≥ 18).
age = int(input('Enter you age: '))
if age < 18 :
  print('You are not eligible for the vote')
else:
  print('You are eligible')

# Write a program to check if a given year is a leap year.
year = int(input('Enter year '))
if year % 100 == 0 and year % 400 == 0:
  print('Its a leap year ')
elif year % 100 == 0:
  print('Its not a leap year ')
elif year % 4 == 0:
  print('Its a leap year')
else:
  print('Its not a leap year')

# Print numbers from 1 to 20 using a for loop.
for i in range(1, 11):
  print(i)

# Print the multiplication table of 5.
num = int(input('Enter number '))
for i in range(1, 11):
  print(f'{num} x {i} = {num * i}')

# Print all even numbers from 1 to 50 using a while loop.
i = 1
while i <= 50:
  if i % 2 == 0:
    print(i)
  i += 1
  

# Take 3 numbers from the user and print the largest.
num1 = int(input('Enter a number here '))
num2 = int(input('Enter a number here '))
num3 = int(input('Enter a number here '))

if num1 > num2 and num1 > num3:
  print('Num 1 is largest ')
elif num2 > num1 and num2 > num3:
  print('Num 2 is the largest')
else:
  print('Num 3 is the largest')

# Take a string and count how many vowels are in it.
str = input('Enter a string here ')
count = 0
for i in str:
  if i == 'a' or i == "e" or i == 'i'or i== 'o' or i == 'u':
    count = count+1
print(count)

# Convert an integer to binary without using bin().
num = int(input('Enter a number here '))
print(format(num, 'b'))

# Write a program to calculate the simple interest.
principal_amount = float(input('Enter principal amount: '))
rate_of_interest = float(input('Enter rate of interest: '))
time = float(input('Enter time: ')) 

simple_interest = (principal_amount * rate_of_interest * time) / 100
print(simple_interest)

# Take two numbers and print the result of every operator: + - * / // % **.
a = 10 
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# 📌 Conditionals

# Take marks of 5 subjects and print the grade:
# 90+ : A
# 80-89 : B
# 70-79 : C
# <70 : Fail

sub1 = float(input('Enter marks: '))
sub2 = float(input('Enter marks: '))
sub3 = float(input('Enter marks: '))
sub4 = float(input('Enter marks: '))
sub5 = float(input('Enter marks: '))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/500 * 100

if percentage >= 90:
  print(percentage, 'A')
elif percentage >= 80 and percentage < 90:
  print(percentage, 'B')
elif percentage >= 70 and percentage < 80:
  print(percentage, 'C')
else:
  print(percentage, 'Fail')

# Check whether a character is uppercase, lowercase, digit, or special symbol.
user_input= input('Enter characters here: ')
if user_input.isupper() == True:
  print('Its upper case ')
elif user_input.islower() == True:
  print('Its in lower case')
elif user_input.isdigit() == True:
  print('Its a digit')
elif user_input.isascii() == True:
  print('its a mixture of ascii codes')
else:
  print('Enter a valid string')

# Check whether three sides form a valid triangle.
a= 10
b = 12
c = 4

if a + b > c and b + c > a and a + c > b:
  print('sides of a valid triangle ')

# 📌 Loops

# Print the sum of digits of a number.
num = int(input('Enter a number here: '))
total = 0
while num > 0:
  digit = num % 10
  total += digit
  num //= 10 
print(total)

# Print the factorial of a given number.
num = int(input('Enter a number here: '))
total = 1
while num > 0:
  total = num * total
  num -= 1
print(total)
  
# Print this pattern:
# *
# **
# ***
# ****
# *****
for i in range(1,6):
  print('*'* i)

# Print the reverse of a number (avoid converting to string).
num = int(input('Enter a nunber here: '))
final = ''
while num > 0:
  reverse = num % 10
  final += str(reverse)
  num //= 10
print(int(final))

num = int(input("Enter a number: "))
rev = 0
digit = num % 10
while num > 0:                          #Chat gpt version
    rev = rev * 10 + digit
    num //= 10
print("Reversed number:", rev)


# ✅ HARD LEVEL
# 📌 Variables / Data Types

# Take a sentence and count how many words start with a vowel.

# Create a dictionary from two lists:
# Example:
# keys = ["name", "age"]
# values = ["Zayn", 21]
# Output → {"name": "Zayn", "age": 21}

# Write a program to remove duplicates from a list without using set().

# 📌 Operators

# Build a simple calculator that supports: + - * / // % ** using if-elif.

# Given a list of numbers, find the second largest number.

# 📌 Conditionals

# Write a program to check if a string is palindrome (without slicing or reversed).

# Nested conditions:
# Given salary and age, decide loan eligibility:

# Age 21–60

# Salary ≥ 25,000

# If salary > 50,000 → premium loan

# Else → standard loan

# 📌 Loops

# Print Fibonacci series up to N terms.

# Count how many times each character appears in a string (use dictionary).

# Print this pattern:

#     *
#    ***
#   *****
#  *******
# *********


# Write a program to find all prime numbers between 1 and 200.

# Write a program that checks whether a number is an Armstrong number.