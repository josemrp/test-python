N = int(input())

if N % 2:
	print ('Weird')
else:
	if N > 1 and N < 6:
		print('Not Weird')
	elif N > 5 and N < 21:
		print('Weird')
	else:
		print('Not Weird')
