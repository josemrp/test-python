evenNumbers = list(range(2, 100, 2))

print(evenNumbers)

print(evenNumbers.pop())
evenNumbers.remove(10)
evenNumbers.insert(1, 3)

print(evenNumbers)
print(evenNumbers[0], evenNumbers[-1])
print(min(evenNumbers), max(evenNumbers), sum(evenNumbers))

print(evenNumbers[:5])
print(evenNumbers[40:])
print(evenNumbers[5:10])

#With this i can edit clon with out edit the original list
cloneNumbers = evenNumbers[:]


cars = ['bmw', 'audi', 'mazda', 'fiat']
print(cars)

cars.append('mitsubishi')

print(sorted(cars))
print(cars)

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.reverse()
print(cars)

tup = tuple('abxcyz')
print(tup)
#Can't append or remove

fruit = {'name': 'Banana', 'color': 'yellow', 'weight': 4}
print(fruit['name'], fruit['color'], fruit['weight'])
fruit['color'] = 'black'
fruit['weight'] = 3.5
print(fruit['name'], fruit['color'], fruit['weight'])

print(fruit.items())
for key, value in fruit.items():
	print(key, value)

