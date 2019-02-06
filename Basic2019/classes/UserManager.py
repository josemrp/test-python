import datetime

class UserManager():
	user_details = []
	messages = []
	base_massage = """Hi {name}, 

	Today is: {today} and you war registered on {registered}"""

	def add_user(self, name):
		name = name[0].upper() + name[1:].lower()
		detail = {
			"name": name,
			"registeredOn": datetime.date.today()
		}
		self.user_details.append(detail)

	def format_date(date):
		return '{d.day}/{d.month}/{d.year}'.format(d=date)

	def make_messages(self):
		if len(self.user_details) > 0:
			for detail in self.user_details:
				name = detail['name']
				#registered = self.format_date(detail['registeredOn'])
				#today = self.format_date(datetime.date.today())
				registered = detail['registeredOn']
				today = datetime.date.today()
				message = self.base_massage.format(
					name = name,
					registered = registered,
					today = today
				)
				self.messages.append(message)
		else:
			print("You don't have users")

	def print_messages(self):
		if len(self.user_details) > 0:
			for msg in self.messages:
				print(msg)
		else:
			print("You don't have messages")
			
