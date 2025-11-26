list = ['zahid', 'parveen', 'zaid', 'zain', 'zainab']

list.append('max')
print(list)

list.insert(6, 'fifi')
print(list)


list.remove('zain')
print(list)

list.pop(2)
print(list)

list.reverse()
print(list)

list.extend(['zaid', 'zain'])
print(list)

list.reverse()
print(list)


list2 = list.copy()
print(list2)

print(list.count('zain'))
print(list.index('zainab'))

list2.clear()
print(list2)

list.sort()
print(list)

list[4] = 'max'
print(list)
