items = [('product1', 20), ('product2', 10), ('product3', 30)]

items.sort(key=lambda x : x)
print(tuple(items))


prices = list(map(lambda x : x[1], items))
print(prices)

items = [('product1', 20), ('product2', 10), ('product3', 30)]
filtered = list(filter(lambda x : x[1]>=20, items))
print(filtered)

values = [x for x in range(1, 10)]
print(values)

values1 = [x*2 for x in range(1, 11)]
print(values1)

values2 = {x : x**2 for x in range (1, 11)}
print(values2)

values3 = {x: x*2 for x in range(1, 11)}
print(values3)


lowercase = lambda x : x.lower()
print(lowercase('ZAIN'))

square = lambda x : x**2
print(square(9))
# lambda is a short form for writing function

numbers = [1, 2, 3, 4, 5, 6, 7]
values5 = list(map(lambda x : x*3, numbers))
print(values5)

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
values6 = list(filter(lambda x : x % 2 == 0 , numbers1  ))
print(values6)

values7 = [x for x in numbers1 if x % 2 == 0]
print(values7)

values8 = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(values8)







