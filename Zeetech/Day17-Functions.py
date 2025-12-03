def full_name (first_name, last_name):
  print(f'Welcome {first_name} {last_name}')

full_name('zain', 'shaikh') #Positional Argument
full_name(last_name='shaikh', first_name='zaid') #Keyword Argument


def student_data (id, name, course, classes = 'zeetech'):
  print(id, name, course, classes)

student_data(1, 'zain', 'web dev') 


#Xargs this will take only values in the arguments 
def emp_data(*values):
  print(values)
  print(type(values))

emp_data(101, 'zain', 'mumbra', 'student', 150000)

#XXarge this will take key value pair in the arguments 
def emp_data(**data):
  print(data)

emp_data(id= 101, name= 'zain', surname= 'shaikh', midname = 'zahid')


#Return keyword is use to return final value from defining part to calling part
def add(a, b):
  c = a + b
  return c

print(add(10, 20))
print(add(40, 60))

def is_palindrome (name):
  reverse = name[::-1]
  if name == reverse:
    return f'{name} is a palindrome'
  else:
    return f'{name} is not a palindrome'
  
print(is_palindrome('zain'))
print(is_palindrome('madam'))
print(is_palindrome('mom'))

def factorial(num):
  fact = 1
  for i in range(1, num+1):
    fact = fact * i
  return(fact)

print(factorial(5))
print(factorial(4))
  
  