class User():
	def __init__(self,first_name,last_name,age='',location='',ocupation=''):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + ' ' + last_name
		self.age = age
		self.location = location
		self.ocupation = ocupation

	def describe_user(self):
		print('\nThis is user info about ' + self.full_name.title() + ':')
		print('First name: ' + self.first_name.title())
		print('Last name: ' + self.last_name.title())
		if self.age != '':
			print('Age: ' + str(self.age))
		if self.location != '':
			print('Location: ' + self.location.title())
		if self.ocupation != '':
			print('Ocupation: ' + self.ocupation)

	def greet_user(self):
		print('Hello, ' + self.first_name.title() + '!')