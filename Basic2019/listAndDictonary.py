print('lists')
list1 = ['Item 1', 'Item 2', 'Item 3']
list1.append('Item 4')
print(list1)
print(list1.pop())
print(list1)
print(list1[1])
print('list not have keys')

print('Dictonary')
dict1 = {'name': 'jose', 'age': 23}
print(dict1)
print(dict1['name'])
dict1[0] = 'Key reference 0'
print(dict1)
dict1['self'] = dict1
print(dict1)
print(dict1['self'])
print(dict1['self']['self']) # And continue
print('dicts are nt index')

print('Tuples')
tup = (('string', 'my string'), ('another', 'another string'))
print(tup)
print(tup[0])
print(tup[0][1])
print('Tuples not support insert')
