def full_name (first_name, last_name):
  print(f'Welcome {first_name} {last_name}')

full_name('zain', 'shaikh') #Positional Argument
full_name(last_name='shaikh', first_name='zaid') #Keyword Argument


def student_data (id, name, course, classes = 'zeetech'):
  print(id, name, course, classes)

student_data(1, 'zain', 'web dev') 

def emp_data(*values):
  print(values)
  print(type(values))

emp_data(101, 'zain', 'mumbra', 'student', 150000)