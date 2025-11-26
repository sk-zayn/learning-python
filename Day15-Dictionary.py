#dictionary stores data in a key index form
#key should be passed as a string
#value should be passed as per data type
#in dictionary key is the index of value 

dict ={
  'name' : 'zain',
  'id' : 101,
  'surname' : 'shaikh'
}

print(type(dict))

dict.pop('id') #we need to give key in pop parameter to remove that key value pair
print(dict)

dict.update(id = 101, middle_name = 'zahid') #you can add key value to the dictionary using update it add the pair at the last
print(dict)

dict.popitem() #it will remove the last key pair value from the dictionary
print(dict)

print(dict.get('student fees')) #with get if the key value is not in the dictionary then also you wont get error it will show none

print(dict['id']) #this is how we print the value using key as an index

print(dict.keys()) #to print all the keys 

print(dict.values())# to print all the values

print(dict.items()) #to print key value pairs of the whole dictionary


for i in dict: # this will only print all the keys in the dictinary
  print(i)


for i in dict.values(): # this will only print all the values in the dictinary
  print(i)

for i in dict.items(): # this will only print all the items in the dictinary but binding each pair in tuple
  print(i)

for i, j in dict.items(): # to print the key value pair normally we need to make 2 variable and print them both
  print(i, j)

dict_copy = dict.copy() #this will make the copy of the string
print(dict_copy)

dict_copy.clear() #this will clear out the whole dictionary
print(dict_copy)

keys = {'name', 'id', 'surname'} 
default = None

output = dict.fromkeys(keys, default)
print(output)

cred = {
  'abc' :'abc123',
  'def' : 'def123',
  'ghi' : 'ghi123',
  'jkl' : 'jkl123'
}

username = input('Enter your username ')
password = input('Enter your password ')

for i, j in cred.items():
  if username == i and password ==j :
    print('Login successful')
    break
else:
  print('Login failed')


student_data = {
  'name' : 'zain',
  'id' : 101,
  'addr' : 'mumbai' 
}
menu = input('Enter v for value and k for keys ')

if menu.lower() == 'k':
  key = input('Enter key here ')
  for i, j in student_data.items():
    if i == key:
      print(j)
elif menu.lower() == 'v':
  value = input('Enter the value here ')
  for i, j in student_data.items():
    k = str(j)
    if value == k:
      print(i)
else:
  print('Enter v or k only ')
