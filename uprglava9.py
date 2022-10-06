class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print('The "' + self.restaurant_name.title() + '" is ' + self.cuisine_type + ' cuisine restaurant.')

	def open_restaurant(self):
		print(self.restaurant_name.title() + ' restaurant is opened.')


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


class Privileges():
	def __init__(self,privileges=['Разрешено добавлять сообщения',
			'Разрешено удалять пользователей',
			'Разрешено банить пользователей']):
		self.privileges = privileges

	def show_privileges(self):
		print('\n')
		for v in self.privileges:
			print(v)


class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges()