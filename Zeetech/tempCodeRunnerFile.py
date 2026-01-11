l1 = [1, 2, 3, 4, 5, 6]
l2 = [5, 6, 7, 8, 9, 2]

l3 = []
def commonNumber(l1, l2):
  for i in l1:
    if i in l2 :
      l3.append(i)
  return(l3)

print(commonNumber(l1, l2))