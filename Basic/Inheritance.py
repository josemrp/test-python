class Father:
	def can_swim(self, rtxt=False):
		if(rtxt):
			return 'Can swim'
		return True

class Mother:
	def can_rum(self, rtxt=False):
		if(rtxt):
			return 'Can rum'
		return True

class Child(Father, Mother):
	def can_sleep(self, rtxt=False):
		if(rtxt):
			return 'Can sleep'
		return True

f = Father()
m = Mother()
c = Child()

print('Father')
print(f.can_swim(True))
#print(f.can_rum(True)) Can't
#print(f.can_sleep(True)) Can't

print('Mother')
#print(m.can_swim(True)) Can't
print(m.can_rum(True))
#print(m.can_sleep(True)) Can't

print('Child')
print(c.can_swim(True))
print(c.can_rum(True))
print(c.can_sleep(True))




