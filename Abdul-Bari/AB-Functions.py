#Default parameter
# it works from right hand side means if you want to give only one default parameter it should be from the right hand side
def add (a=1, b=5, c=2):
  print(a + b + c)

add(7)

#positional + keyword arguments (positional arguments need to be before keyword arguments)
def add (a, b, c):
  print(a + b + c)

add(10, c=2, b=5)

#unpacking arguments
def printing(a, b, c):
  print(a, b, c)

l1 = [1, 2, 3, 4, 5]
printing(l1[1], l1[4], l1[2]) #using index to pass the iterable value in the function parrameter

# printing(*l1)#using * to iterate values and pass the values in the function parameter
# only if the iterable value has the same no of elements as the parameters






