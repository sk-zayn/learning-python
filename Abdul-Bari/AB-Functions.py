#Default parameter
# it works from right hand side means if you want to give only one default parameter it should be from the right hand side 
def add (a=1, b=5, c=2):
  print(a + b + c)

add(7)

#positional + keyword arguments (positional arguments need to be before keyword arguments)
def add (a, b, c):
  print(a + b + c)

add(10, c=2, b=5)


