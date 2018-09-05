#Simple functions whit simple params
def ask_ok(prompt, retries=4, reminder='Please try again!'):
	while True:
		#input take a string and display SO and get SI
		ok = input(prompt)
		if ok in ('y', 'yes'):
			return True
		if ok in ('n', 'no'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('Invalid user response')
		print(reminder)

#function whit any arguments and keywords arguments
def cheeseshop(kind, *arguments, **keywords):
	print('-- Do you have any', kind, '?')
	for arg in arguments:
		print(arg)
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw, ':', keywords[kw])

if(ask_ok('Do you want go to cheeseshop?')):
	cheeseshop('Potato', 'It is bad', 'It is very very bad :(', food='Potato', cost='50$', time='now')



