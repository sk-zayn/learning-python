#Tuples are immutable 
#2 tuples can be merged together
#for single value we need to put comma or else it wont be count as tuple
#tuple is also iterable

tup1 = (1, 2, 3, 4, 5, 5, 5)
print(tup1)
print(type(tup1))

tup2 = (6, 7, 8, 9)
tup3 = tup1 + tup2
print(tup3)

print(tup3.count(5))
print(tup3.index(5))