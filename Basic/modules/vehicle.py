class Car:
	maxSpeed = 300 
	def __init__(self, owner):
		self.owner = owner
		self.speed = 0
	def accelerate(self, value):
		self.speed += value
		if self.speed > self.maxSpeed:
			self.speed = self.maxSpeed
	def decelerate(self, value):		
		self.speed -= value
		if self.speed < 0:
			self.speed = 0
	def getStatus(self):
		print("Owner:", self.owner, "current speed:", self.speed)
