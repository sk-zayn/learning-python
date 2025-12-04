# list2 = list((1, 2, 3, 'A', 'b', True))
# print(list2)

list1 = [3, 4, 5, 6, 7]
# list7 =[1, 3]
# list3 = list2 + list1
# print(list3)

# list4 = list1 + list2 + list3
# print(list4)
# list1 * 4
# print(list1)

for i in range( len(list1)): # to print indexes of the list 
  print(i)

list1.insert(45, 2)
list1.extend({1, 2, 3, 4, 5, 4, 5, 5, 6, 4, 3, 3, 4})

l2 = [x for x in range(10)]
print(l2)

# l1 = []
# i = 1
# while i > 0 :
#   inp = input ('To enter name press e to print list press y')
#   if inp.lower() == 'e':
#     names = input('Enter a name here: ')

l1 = input('Enter a name: ').split()
print(l1)

l2 = [x for x in range(1, 11)]
print(l2)



l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
l3 = []
for i in range(len(l1)):
  s = []
  for j in range(len(l1[i])):
    s.append(l1[i][j] + l2[i][j])
  l3.append(s)
print(l3)
    
  
