items = [('product1', 20), ('product2', 10), ('product3', 30)]

items.sort(key=lambda x : x)
print(tuple(items))


prices = list(map(lambda x : x[1], items))
print(prices)

items = [('product1', 20), ('product2', 10), ('product3', 30)]
filtered = list(filter(lambda x : x[1]>=20, items))
print(filtered)


