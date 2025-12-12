#Default parameter
# it works from right hand side means if you want to give only one default parameter it should be from the right hand side
def add (a=1, b=5, c=2):
  print(a + b + c)

add()

#positional + keyword arguments (positional arguments need to be before keyword arguments)
def add (a, b, c):
  print(a + b + c)

add(10, c=2, b=5)


#unpacking arguments
def printing(a, b, *c): # using * to give more than one value to the variable and it will be in the form of tuple
  return a, b, c

print(printing(10, 20, 30, 40, 50, 50, 4, 3, 2, 1)) #a and b are at the starting so we have to give positional values to those
# if a had the star then we would have to give keyword argument to b and c (these are the positional arguments which will returns us tuple)


l1 = [1, 2, 3, 4, 5]
printing(l1[1], l1[4], l1[2]) #using index to pass the iterable value in the function parrameter

# printing(*l1)#using * to iterate values and pass the values in the function parameter
# only if the iterable value has the same no of elements as the parameters

def fun2(**kwargs): #we use ** to give as many args as we want but in keyword form
  print(kwargs)

fun2(name= 'zain', roll= 20, add= 'mumbai') #using keyword arguments will give us dictionary



def add(a, b, c):
  x, y, z =1, 2, 3
  print(locals())

add(5, 6, 7)

print(globals())

