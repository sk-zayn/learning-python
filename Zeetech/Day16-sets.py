# Sets will not contain duplicate values 
# sets dosent support indexing
# set1 = {10, 20, 30, 40, 40, 50, 10, 20}
# print(set1)

# set2 = {10, 20, 30, 40}
# set3 = {30, 40, 50, 60, 70}
# print(set2 | set3) #union combines sets 
# print(set2 & set3) #interrsection common values from two sets
# print(set2 - set3) #difference
# print(set3 - set2) #difference
# print(set2 ^ set3) #uncommon 

# enumerate
# it fetches both index and values

# list = ['zain', 'zahid', 'zainab', 'zaid', 'parveen']
# for i, j in enumerate(list):
#   print(i, j)

# # zip
# it needs 2 or more list to work it will join the index value of both like 1:1 and return it and do the same for rest

# student = ['zain', 'zahid', 'zainab', 'zaid', 'parveen']
# born = ['2nd born', 'father', '3rd born', '1st born', 'mother']

# for i, j in zip(student,born):
#   print(i, j)

# numbers = [5, 4, 3]
# factorial =[]
# for i in numbers:
#   fact = 1
#   for j in range(1, i+1):
#     fact = fact * j
#   factorial.append(fact)
# print(factorial)

# prime = []
# for i in range(2, 101):
#   for j in range(2, i):
#     if i % j == 0:
#       break
#   else:
#     prime.append(i)
# print(prime [0:7])

# list = ['madam', 'zaid', 'zain', 'mam', 'mom']
# list2 = []

# for i in list:
#   reverse = i [::-1]
#   if i == reverse :
#     list2.append('is palindrome')
#   else:
#     list2.append('is not a palindrome')

# for i, j in zip(list, list2):
#   print(i, j)

  