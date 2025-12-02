# Any thing that is written in quotes can be called string 
# Operators in string
'''
1. concatination
2. Repetition
3. indexing
4. slicing
5. in 
6. not in
'''

# # 1. concatinate there are 2 methods using +operator and ""

# s1 = 'hello'
# s2= 'world'
# s3 = s1 + s2
# print(s3)

# s5 = 'hello' 'world'
# print(s5)

# print(dir(str))# dir is a function that prints all the method you can use for the given parameter

# s = 'Hi how are you, what are you doing tomorrow, lets play volleyball '
# x = len(s)
# count = 0
# print(s.find('y'))
# for i in range(x+1):
#     if s.find('o') == True:
#         print(s[i])
#         count += 1

# s = 'Hi how are you, what are you doing tomorrow, lets play volleyball '
# index = 0

# while True:
#     pos = s.find('y', index)
#     if pos == -1:
#         break
#     print("y at index", pos)
#     index = pos + 1

# s= '.....hi '
# print(s.strip())

# s = 'akdjfkwuekndfkiufksbmxnxuso'
# s1 = sorted(s)
# print(s1)

# s2 = "".join(s1)
# print(s2)
# print(s2.count('a','b'))

# item_name = input('Enter item name: ')
# price = input('Enter price: ')
# total = len(item_name) + len(price)
# dots = '.' * (25 - total)
# print(item_name + dots + price)


# password = input('Enter password: ')
# confirm = input('Confirm password: ')
# if password == confirm:
#   print('Access granted')
# else:
#   print('Wrong password')

# card = input('Enter card no: ')
# last_digit = card[15:]
# star = '*' * 4
# print(star + ' ' + star + ' ' + star + ' ' + last_digit)

# email = input ('Enter email id: ')
# position = email.find('@')
# print(position)
# user_name = email[:position]
# domain_name = email[position + 1:]
# print('username =', user_name)
# print('domain name =', domain_name)

# string = input('Enter a string here: ')
# s = string[:-1]
# print(s)


# if string[:] == string[::-1]:
#   print('Your sting is palindrome ')
# else:
#   print('Your string is not a palindrome')

# s1 = input('Enter word: ')
# s2 = input('Enter word: ')
# ss1 = sorted(s1)
# ss2 = sorted(s2)
# if ss1 == ss2:
#   print('Its anagram')
# else:
#   print('Its not anagram')

# s1 = input('Enter String: ')
# lower = ''
# upper = ''
# for i in s1:
#   if i == i.lower():
#     lower = lower + i
#   else:
#     upper = upper + i
# print(lower + upper)


s5 = input('Enter a string: ')
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
for p in punctuation:
    s5 = s5.replace(p,'')
print(s5)