dict1 = {"101":'zain', 102: 'zaid', 103: 'zainab'}
print(dict['101'])  #can only pass key to get the value of that particular key
# print(dict['zain'])  #if value is passed error will be thrown

dictionary = dict() #a way to create dictionary
print(type(dictionary))

for i in range(1, 6):  #a way to add value in dictionary using loops
  dictionary[i] = i**2
print(dictionary)

dictionary1 = {} #a way to create empty dictionary

dictionary1 = dict(((101, 'zain'), (102, 'zainab'), (103, 'zahid'))) #a way to add value in an empty dictionary using tuple or any iterable
#cause you can only pass one value in the dictionary function and then again a tuple or any iterable to form a key value pair

dictionary2 = dict(([101, 'zain'], [102, 'zainab'], [103, 'zahid'])) #a way to add value in an empty dictionary using tuple or any iterable
#cause you can only pass one value in the dictionary function and then again a tuple or any iterable to form a key value pair
print(dictionary1)
print(dictionary2)


#zip function
#only the pairing values will be there in dictionary excess values will be ignored and no error will be thrown
#we can use different iterable data types to create one dictionary
l1 = [1, 2, 3, 4, 5]
l2 = ['apple', 'ball' , 'cat', 'dog', 'elephant']
dictionary3 = dict(zip(l1 ,l2))
print(dictionary3)

# enumerate for dictionary
# key value seperated by colon and everytthing will be same as list or set or tuple
dict2 = {x: x**2 for x in range(1, 6)}
print(type(dict2))
print(dict2)

# to make a dictionary using zip you can create iterables inside the zip function
# and create outside and pass it in the zip function also
dict3 = {x : y for x, y in zip([1, 2, 3, 4], ['zain', 'zaid', 'zainab', 'zahid'])}
print(dict3)

#enumerate function give 2 values 1 index and 2 value
name = 'zain'
dict4 = {x : y for x, y in enumerate(name)}
print(dict4)

dict1 = {"101":'zain', 102: 'zaid', 103: 'zainab'}
print(dict1.keys()) #returns list of keys
print(dict1.values()) #returns list of values
print(dict1.items()) #returns list of key value pair encoded in tuple

for k in dict1.keys(): #to iterate over keys of the dictionary
  print(k)

for v in dict1.values(): #to iterate over values of the dictionary
  print(v)

for k, v in dict1.items(): #taking 2 variable 1 to iterate on the keys and another one to iterate over  value
  print(k, v)



s1 = {1, 2, 3, 4, 5}
s2 = {'zain', 'zaid', 'zainab', 'zahid', 'parveen'}
dict0 = {x : y for x, y in zip(s1,s2)}
print(dict0)





