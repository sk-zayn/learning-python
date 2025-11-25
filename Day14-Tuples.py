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

a = 5
b = 7

# temp = a 
# a = b
# b = temp

(a,b) = (b,a)
print(a)
print(b)

#unpacking

list3 = [12, 23, 34, 45, 56, 67,78, 89, 90]
var1, var2, *var3, var4 = list3
print(var1)
print(var2)
print(var3)
print(var4)
