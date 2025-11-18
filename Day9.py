list = ["zain", "zaid", "zainab", "zahid", "parveen"]
for name in list : #name is iterator and list is iterable, iterator visits iterable and perform the given function until the list is over.
  print(name)
else : #in python we can use else of loops also it will run when the condition goes false like here it will print every naem in the list and when list is over it will print else statement.
  print("list is over")


# Range it takes 3 parameter 1st starting point 2nd ending point 3rd gap between them.

for i in range(1, 51, 2) :# goes from 1 to 50 and leave 1 number in between 1,3,5,7,9...49
  print(i)

list =[]
for i in range(1, 51, 2) :# goes from 1 to 50 and leave 1 number in between 1,3,5,7,9...49
  list.append(i) #append adds the new output at the end of the list 
  print(list)

list1 = ["zain", 19, 12, 20.6, 49.0, "zahid", "parveen"]
list2 = []
for i in list1: #iterate on all the index in list and store it in i
  if type(i) == str : # check the type of the i if its string then the condition is true 
    list2.append (i) # add it in the list2
print (list2)


list = [10, 20, 30, 40]
list1 = [20, 40, 60, 80]
list2 = []

for i in list:
  if i in list1:
    list2.append(i)
print(list2)





