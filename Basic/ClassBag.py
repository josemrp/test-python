class Bag:
	def __init__(self, name='Simple bag'):
		self.data = []
		self.name = name

	def add(self, item):
		self.data.append(item)

x = Bag('X bag')
y = Bag()

x.add(1)
x.add(2)
x.add(3)
x.add(4)

y.add(2)
y.add(4)

print('Objects')
print(x)
print(y)

print('Names')
print(x.name)
print(y.name)

print('Data')
print(x.data)
print(y.data)


