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


