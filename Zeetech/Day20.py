# import json
# import sqlite3
# import getpass

# emailId = input('Enter email-id here: ')
# userName = emailId.split('@')[0]
# password = input('Enter password here: ')

# conn = sqlite3.connect('db.sqlite3')
# query = 'insert into Register values (?,?,?)'
# conn.execute(query, [emailId, userName, password])
# conn.commit()
# print('Data has been inserted successfully')


#Exception Handling
#exception are runtime error
#exception handling means instead of error running a meaning ful message

# try block : we write in here that can generate an Error
#except block : we write in here a message that should be shown in case of error
#finally block : you will be quiting a session or else closing a file


# try:
#   age = int(input('Enter your age: '))
#   print(age)
# except ValueError:
#   print('Age cannot be characters ')
# else:
#   print('No exception found')


# try:
#   age = int(input('Enter your age: '))
#   income = 50000
#   risk = income / age
#   print(age)
#   print(risk)
# except ZeroDivisionError:
#   print('Age cannot be 0')
# except ValueError:
#   print('Age cannot be characters ')
# else:
#   print('No exception found')

try:
  with open ('file.txt', 'r')as file: #using with open the file will be closed automatically we dont need to do it manually with finally ()
    file_content1 = file.read() #print the whole file at once
    file_content = file.readline() #print one line at a time
    file_content2 = file.readlines() #print all the line in the form of list and /n for next line
    print(file_content)
except FileNotFoundError:
  print('File does not exist')
else:
  print('File exists')

with open('file2.txt', 'w') as file: #write function creates a new file and add the content in it
  file.write('I am a python developer ') #if we try to add another content after running the file it will override the content added before
# to add the text in the previous file we use append method instead of write

with open('file2.txt', 'a') as file:
  file.write('I am a python developer ')

def is_age_criteria(age):
  try:
    if age < 18:
      raise ValueError('We dont hire minors')
  except ValueError as e :
    print(e)
  else:
    print('You are welcome here')

is_age_criteria(12)
is_age_criteria(25)


