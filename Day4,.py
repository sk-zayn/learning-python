# In python there are two types of function (direct functions and imported function)

# import math

# print(math.floor(80.2)) #.floor takes the lowest value 
# print (math.ceil(80.1)) #.ceil takes the highest value

# print(math.sqrt(25)) #gives you square root
# print(math.cbrt(64)) #gives you cube root
# print(math.factorial(5)) #gives you factorial 5*4*3*2*1


# Conditional Statement

# Question 1
# age = int(input("Enter your age "))
# if age >= 18 :
#     print("you are major")
# else:
#     print("you are minor ")

# Question 2
# num1 = int(input("enter the number "))
# num2 = int (input("enter the number "))
# if num1 > num2 :
#     print("num 1 is greater ")
# elif num2 > num1 :
#     print("num 2 is greater ")
# else :
#     print("both are equal")

# Question 3
# num1 = int(input("enter the number "))
# num2 = int (input("enter the number "))
# if num1 < num2 :
#     print("num 1 is smaller ")
# elif num2 < num1 :
#     print("num 2 is smaller ")
# else :
#     print("both are equal")

# Question 4
# num = int (input("enter number here "))
# if num > 100 :
#     print(num)
# else :
#     print("your number is less than 100")


# Question 5
# num = int (input("enter number here "))
# if num % 2 == 0:
#     print("It's even")
# else:
#     print("It's odd")

# Question 6
# num = int (input("enter number here "))

# if num<0 :
#     print("its a negative number")
# elif num > 0 :
#     print ("its a positive number")
# else :
#     print ("its a zero")

# Question 7
# num = int (input("enter number here "))

# if num < 100 :
#     print("number is too small")
# elif num > 100 :
#     print ("number is too large")
# else :
#     print ("we think alike")

# Question 8
# max = 80
# maximum_number = 80*4
# sub1 = int (input("enter the marks of sub 1 "))
# sub2 = int (input("enter the marks of sub 2 "))
# sub3 = int (input("enter the marks of sub 3 "))
# sub4 = int (input("enter the marks of sub 4 "))

# subjects = sub1+sub2+sub3+sub4
# percentage = (subjects/maximum_number) * 100

# if (sub1<=80) and (sub2<=80) and (sub3<=80) and (sub4<=80):
#     print(f"Total marks {subjects} / {maximum_number}")
#     print(f"Percentage {percentage}")
#     if percentage >= 80:
#         print("very well done")
# else :
#     print("please enter the correct marks")

# Question 9
# age = int (input ("enter your age "))
# if age <= 12:
#     print("you are a child")
# elif age >= 13 and age <= 19:
#     print("you are a child")
# elif age >= 20 and age <= 59:
#     print("you are a child")
# else:
#     print("you are a senior citizen")

# num = int (input ("Enter your number "))
# if num % 4 == 0 :
#   if num % 5 == 0:
#     print (f"{num} is divisible by 4 and 5")
#   else :
#     print(f"{num} is not divisible by 5")
# else :
#   print(f"{num} is not divisible by 4")


has_salary_slip = True
has_good_cibil_score = True
has_itr = False

if has_salary_slip and has_good_cibil_score or has_itr :
  print("You are eligible to get the loan")
else:
  print("You are not eligible to get the loan")