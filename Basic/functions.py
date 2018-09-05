#Basic function
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

#execute
fib(10)

#convert var in a function
f = fib
f(20)

#this function dos'nt return but in print retrun None
print(f(0))

#Same function wiht returns 
def rfib(n):
	a, b = 0, 1
	result = []
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

f100 = rfib(100)
print('return', end=' ')
print(f100)

