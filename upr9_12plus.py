from upr9_12 import User

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