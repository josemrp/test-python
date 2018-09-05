import math

arguments = input()
arg = arguments.split(' ')

welcome = 'WELCOME'
paloma = '.|.'
N = int(arg[0])
M = int(arg[1])

if N * 3 == M and N % 2:
	n = int((N-1)/2)
	m = int((M-1)/2)
	isBeforeWelcome = True
	k = 0

	for i in range(N):
		for j in range(M):

			l = (3*k) + 1

			if i == n and j >= m-3 and j <= m+3:
				print(welcome[j+3-m], end='')

			elif j >= m-l and j <= m+l and i != n:

				index = j+l-m
				while(index > 2):
					index = index-3
				
				print(paloma[index], end='')

			else: 
				print('-', end='')
		
		if i == n:
			isBeforeWelcome = False			
	
		k = k+1 if isBeforeWelcome else k-1	
		
		print('')
