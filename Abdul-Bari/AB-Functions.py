# #Default parameter
# # it works from right hand side means if you want to give only one default parameter it should be from the right hand side
# def add (a=1, b=5, c=2):
#   print(a + b + c)

# add()

# #positional + keyword arguments (positional arguments need to be before keyword arguments)
# def add (a, b, c):
#   print(a + b + c)

# add(10, c=2, b=5)


# #unpacking arguments
# def printing(a, b, *c): # using * to give more than one value to the variable and it will be in the form of tuple
#   return a, b, c

# print(printing(10, 20, 30, 40, 50, 50, 4, 3, 2, 1)) #a and b are at the starting so we have to give positional values to those
# # if a had the star then we would have to give keyword argument to b and c (these are the positional arguments which will returns us tuple)


# l1 = [1, 2, 3, 4, 5]
# printing(l1[1], l1[4], l1[2]) #using index to pass the iterable value in the function parrameter

# # printing(*l1)#using * to iterate values and pass the values in the function parameter
# # only if the iterable value has the same no of elements as the parameters

# def fun2(**kwargs): #we use ** to give as many args as we want but in keyword form
#   print(kwargs)

# fun2(name= 'zain', roll= 20, add= 'mumbai') #using keyword arguments will give us dictionary



# def add(a, b, c):
#   x, y, z =1, 2, 3
#   print(locals())

# add(5, 6, 7)

# print(globals())

# def maximum_limit(a, b):
#   if abs(a-b) <= 5 :
#     return True
#   else:
#     return False

# print(maximum_limit(2, 4))


# def largest_number(a, b, c):
#   if a > b and a > c:
#     return f'{a} is the largest number'
#   elif b > a and b > c:
#     return f'{b} is the largest number'
#   else:
#     return f'{c} is the largest number'

# print(largest_number(4, 6, 2))
# print(largest_number(2, 4, 8))
# print(largest_number(8, 4, 2))

# def intro(name, profession, /):# back slash is use when you want the parameter to be positional only
# # when slash is there you cant give keyword parameters
#   return f'Hii my name is {name} and i am a {profession}'

# print(intro('zain', 'student'))


# def planet_finder(id):
#   planets = {
#     1 : 'Mercury',
#     2 : 'Venus',
#     3 : 'Earth',
#     4 : 'Mars',
#     5 : 'Jupiter',
#     6 : 'Saturn',
#     7 : 'Uranus',
#     8 : 'Neptune',
#     9 : 'Pluto'
#   }
#   if id > 0 and id < 9:
#     return planets[id]
#   else:
#     return 'invalid id'

# id = int(input('Enter the planet id here: '))
# p = planet_finder(id)
# print('your planet is ', p)

# l1 = [100, 545, 340, 345, 678, 32, 20, 600]

# def add_zeros(l1):
#   sum = 0
#   for i in l1:
#     if i % 10 == 0:
#       sum += i
#   return sum

# print(add_zeros(l1))

# d = {'a':10, 'b':20, 'c':30, 'd':40}

# def invert (d):
#   newd = {}
#   for k, v in d.items():
#     newd[v] = k
#   return newd


# print(invert(d))

# set1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def pangram(sen):
#   set2 = set(sen)
#   set2.discard(' ')
#   set3 = sorted(set2)
#   print(set3)
#   if set3 == set1:
#     return 'The given sentence is pangram'
#   else:
#     return 'The given sentence is not a pangram'

# print(pangram('the quick brown fox jumps over the lazy dog'))


sentence = ('My Name Is Zain Zahid Shaikh FDERT')
# def case_count (sentence):
#   sen1 = sentence.replace(' ','')
#   lower_case = ''
#   upper_case = ''
#   for i in sen1:
#     if i.islower() == True:
#       lower_case += i
#     else:
#       upper_case += i
#   return f'count of lower case is {len(lower_case)}, count of upper case is {len(upper_case)}'

# print(case_count(sentence))

# def count (sen):
#   upper = 0
#   lower = 0
#   for i in sen:
#     if i.islower() == True:
#       lower += 1
#     elif i.isupper() == True:
#       upper += 1
#   return lower, upper

# print(count(sentence))

def smallest (*args, low_limit = 0):
  if low_limit == None:
    return min(args)
  else:
    list =[x for x in args if x >= low_limit]
    return min(list)

print(smallest(5, 3, 4, 7))
print(smallest(1, 3, 5, -6, 4))

def pascal(n):
  r = [1]

  for i in range(n):
    print(r)
    tr = [0] + r
    r = r + [0]
    nr = [x+y for x, y in zip(r, tr)]
    r = nr

pascal(8)
