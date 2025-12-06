# # list2 = list((1, 2, 3, 'A', 'b', True))
# # print(list2)

# list1 = [3, 4, 5, 6, 7]
# # list7 =[1, 3]
# # list3 = list2 + list1
# # print(list3)

# # list4 = list1 + list2 + list3
# # print(list4)
# # list1 * 4
# # print(list1)

# for i in range( len(list1)): # to print indexes of the list 
#   print(i)

# list1.insert(45, 2)
# list1.extend({1, 2, 3, 4, 5, 4, 5, 5, 6, 4, 3, 3, 4})

# l2 = [x for x in range(10)]
# print(l2)

# # l1 = []
# # i = 1
# # while i > 0 :
# #   inp = input ('To enter name press e to print list press y')
# #   if inp.lower() == 'e':
# #     names = input('Enter a name here: ')

# l1 = input('Enter a name: ').split()
# print(l1)

# l2 = [x for x in range(1, 11)]
# print(l2)



# l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# l3 = []
# for i in range(len(l1)):
#   s = []
#   for j in range(len(l1[i])):
#     s.append(l1[i][j] + l2[i][j])
#   l3.append(s)
# print(l3)
    
# work_hour =[int(x) for x in input('Enter number of hours you worked in a week seperated by space: ').split()]
# print(work_hour) 
# per_hour_pay = int(input('Enter per hour pay: '))
# total_time = 0
# for i in work_hour:
#   total_time += i

# salary_of_the_week = total_time * per_hour_pay
# print(f'Your salary for this week is {salary_of_the_week}')




# work_hour =[int(x) for x in input('Enter number of hours you worked in a week seperated by space: ').split()]
# sum_of_hours = sum(work_hour)# this will give us sum of work hous so we wont have to use loop to iterate and add element in total time
# per_hour_pay = int(input('Enter per hour pay: '))

# salary_of_the_week = sum_of_hours * per_hour_pay
# print(salary_of_the_week)

# l1 = [1, 2, 5, 3, 2, 8, 9, 6, 9, 1, 7, 3 ,7]
# l2 = []
# [l2.append(i) for i in l1 if i not in l2 ] #this is how to write a one line code
# print(sorted(l2))

# for i in l1:
#   if i not in l2:
#     l2.append(i)

# l2.sort()
# print(l2)   # you cant print and sort in one sentence using sort()
# print(sorted(l2)) #you have to usr sorted function

# l1 = [2, 3, 7, 8, 3, 2]
# number = ''
# for i in l1:
#   number += str(i)

# print(int(number))

# fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
# fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']
# index1 = 10
# index2 = 10
# for i in range(len(fav1)):
#   indx = fav2.index(fav1[i])

#   if (i + indx) < (index1 + index2):
#     index1 = i 
#     index2 = indx
  
# print(fav1[index1], index1 + index2)


# l1 = [6, 7, 9, 10, 4, 3, 5]
# l2 = [2, 4, 8, 0, 6, 9]
# l3 = []
# [l3.append(x) for x in l1 if x  in l2]
# print(l3)

# l = ['a', 'v', 'a', 'r', 'e', 'a', 'e', 'a', 'v', 'w', 'r']
# result = []
# for i in l:
#   a = (i, l.count(i))
#   if a not in result:
#     result.append(a)
# print(result)


# l2 = sorted(set(l))
# l3 = []
# for i in l2:
#   x = l.count(i)
#   l4 = list(i, x)
# print(i, x)
# print(l4)


# l1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
# l2 = [] 
# for i in range(4):
#   s = []
#   for j in range(3):
#     s.append(l1[j][i])
#   l2.append(s)

# print(l2)

# fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
# char = input('Enter the first character of the food: ').lower()
# [print(i) for i in fav1 if i[0] == char]





t1 = 10, 'zain', 40+2j, True, 40.8
print(type(t1), t1)
a, b, c = t1
print(a, b, c)
