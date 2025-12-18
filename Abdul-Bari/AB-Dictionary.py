# dict1 = {"101":'zain', 102: 'zaid', 103: 'zainab'}
# print(dict['101'])  #can only pass key to get the value of that particular key
# # print(dict['zain'])  #if value is passed error will be thrown

# dictionary = dict() #a way to create dictionary
# print(type(dictionary))

# for i in range(1, 6):  #a way to add value in dictionary using loops
#   dictionary[i] = i**2
# print(dictionary)

# dictionary1 = {} #a way to create empty dictionary

# dictionary1 = dict(((101, 'zain'), (102, 'zainab'), (103, 'zahid'))) #a way to add value in an empty dictionary using tuple or any iterable
# #cause you can only pass one value in the dictionary function and then again a tuple or any iterable to form a key value pair

# dictionary2 = dict(([101, 'zain'], [102, 'zainab'], [103, 'zahid'])) #a way to add value in an empty dictionary using tuple or any iterable
# #cause you can only pass one value in the dictionary function and then again a tuple or any iterable to form a key value pair
# print(dictionary1)
# print(dictionary2)


# #zip function
# #only the pairing values will be there in dictionary excess values will be ignored and no error will be thrown
# #we can use different iterable data types to create one dictionary
# l1 = [1, 2, 3, 4, 5]
# l2 = ['apple', 'ball' , 'cat', 'dog', 'elephant']
# dictionary3 = dict(zip(l1 ,l2))
# print(dictionary3)

# # enumerate for dictionary
# # key value seperated by colon and everytthing will be same as list or set or tuple
# dict2 = {x: x**2 for x in range(1, 6)}
# print(type(dict2))
# print(dict2)

# # to make a dictionary using zip you can create iterables inside the zip function
# # and create outside and pass it in the zip function also
# dict3 = {x : y for x, y in zip([1, 2, 3, 4], ['zain', 'zaid', 'zainab', 'zahid'])}
# print(dict3)

# #enumerate function give 2 values 1 index and 2 value
# name = 'zain'
# dict4 = {x : y for x, y in enumerate(name)}
# print(dict4)

# dict1 = {"101":'zain', 102: 'zaid', 103: 'zainab'}
# print(dict1.keys()) #returns list of keys
# print(dict1.values()) #returns list of values
# print(dict1.items()) #returns list of key value pair encoded in tuple

# for k in dict1.keys(): #to iterate over keys of the dictionary
#   print(k)

# for v in dict1.values(): #to iterate over values of the dictionary
#   print(v)

# for k, v in dict1.items(): #taking 2 variable 1 to iterate on the keys and another one to iterate over  value
#   print(k, v)



# s1 = {1, 2, 3, 4, 5}
# s2 = {'zain', 'zaid', 'zainab', 'zahid', 'parveen'}
# dict0 = {x : y for x, y in zip(s1,s2)}
# print(id(dict0[5]))

# dict9 = {
#   'sachin' :' 12/8/2012',
#   'arhan' : '13/2/1998',
#   'zain' : '12/9/2003',
#   'zainab' :'21/8/2006',
#   'zaid' :' 4/5/2002'
# }
# name = input('Enter your name: ')
# for i in dict9.keys():
#   if i == name:
#     print(dict9[i])
#     break

# data = {
#     "introduction": "My name is Zayn and I love learning new things.",
#     "daily_routine": "I usually start my day around 11:30 AM.",
#     "hobby": "I enjoy playing football in the evenings.",
#     "goal": "I want to become a software engineer in the future.",
#     "pet_story": "I have two adorable cats named Max and FiFi who keep me active.",
#     "travel_dream": "One day, I hope to visit Japan and explore its culture.",
#     "study_plan": "Right now, I am learning Python and preparing to switch to Java for DSA."
# }
# dataKeys = data.keys()
# dataValues = data.values()

# print(max(dataKeys, key=len))
# print(max(dataValues, key=len))


# take input of counry name from the user and print it in a dictionary alphabetically

countries = {}
for i in range(5):
  name = input('Enter a country name here: ')
  if name[0].upper() not in countries:
    countries[name[0].upper()] = [name]
  else:
    countries[name[0].upper()].append(name)

print(countries)

# romanNumbers = {
#   'I' : 1,
#   'V' : 5,
#   'X' : 10,
#   'L' : 50,
#   'C' : 100,
#   'D' : 500,
#   'M' : 1000
# }

# s1 = 'CDXLIV'
# total = 0

# for i in range(len(s1)):
#   value = romanNumbers[s1[i]]

#     # If next value exists and is bigger → subtract
#   if i + 1 < len(s1) and romanNumbers[s1[i+1]] > value:
#     total -= value
#   else:
#     total += value

# print(total)



# name = input('Enter your name: ')
# rollNo = int(input('Enter your roll no: '))
# departmentName = input('Enter your department name: ')

# students = {}
# if name not in students:
#   pair = {
#     'name' : name,
#     'rollno' : rollNo,
#     'Deparment' : departmentName
#   }
#   students.setdefault(name, pair)

# print(students)


# students = {}

# while True:
#     name = input('Enter your name: ')
#     rollNo = int(input('Enter your roll no: '))
#     departmentName = input('Enter your department name: ')

#     students[name] = {
#         'name': name,
#         'roll no': rollNo,
#         'Department': departmentName
#     }

#     more = input("Add more students? (yes/no): ").lower()
#     if more != "yes":
#         break

# print(students)
print('hi')

