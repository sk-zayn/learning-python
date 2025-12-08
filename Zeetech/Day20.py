import json
import sqlite3
import getpass

emailId = input('Enter email-id here: ')
userName = emailId.split('@')[0]
password = input('Enter password here: ')

conn = sqlite3.connect('db.sqlite3')
query = 'insert into Register values (?,?,?)'
conn.execute(query, [emailId, userName, password])
conn.commit()
print('Data has been inserted successfully')


#Exception Handling
#exception are runtime error
#exception handling means instead of error running a meaning ful message

# try block : we write in here that can generate an Error
#except block : we write in here a message that should be shown in case of error
#finally block : you will be quiting a session or else closing a file


try:
  age = int(input('Enter your age: '))
  print(age)
except ValueError:
  print('Age cannot be characters ')
else:
  print('No exception found')

