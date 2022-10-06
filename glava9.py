# 28/03/2022 Начинаю изучать классы

#upr_9_1

class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print('The "' + self.restaurant_name.title() + '" is ' + self.cuisine_type + ' cuisine restaurant.')

	def open_restaurant(self):
		print(self.restaurant_name.title() + ' restaurant is opened.')

restaurant = Restaurant('tokio city','japanese')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
Restaurant.describe_restaurant(restaurant)
Restaurant.open_restaurant(restaurant)

#upr_9_2

class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print('The "' + self.restaurant_name.title() + '" is ' + self.cuisine_type + ' cuisine restaurant.')

	def open_restaurant(self):
		print(self.restaurant_name.title() + ' restaurant is opened.')

tokio = Restaurant('tokio city','japanese')
sofa = Restaurant('sofa bar','russian')
crystal = Restaurant('crystal','european')

Restaurant.describe_restaurant(tokio)
Restaurant.describe_restaurant(sofa)
Restaurant.describe_restaurant(crystal)

#upr_9_3

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

olyalya = User('olga','kartashova',location='murmansk')
di = User('diana','berchuk',22,'saint-petersburg')
brolya = User('olga','berchuk')
chebilya = User('ilya','cheburov',30,ocupation='programer')

User.describe_user(olyalya)
User.describe_user(brolya)
User.describe_user(di)
User.describe_user(chebilya)

User.greet_user(olyalya)
User.greet_user(di)
User.greet_user(brolya)
User.greet_user(chebilya)

#upr_9_4

class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('The "' + self.restaurant_name.title() + '" is ' + self.cuisine_type + ' cuisine restaurant.')

	def open_restaurant(self):
		print(self.restaurant_name.title() + ' restaurant is opened.')

	def set_number_served(self,number):
		self.number_served = number

	def increment_number_served(self,incr_number):
		self.number_served += incr_number

restaurant = Restaurant('tokio city','japanese')
print(restaurant.number_served)
restaurant.number_served = 4
print(restaurant.number_served)
Restaurant.set_number_served(restaurant,7)
print(restaurant.number_served)
Restaurant.increment_number_served(restaurant,74)
print(restaurant.number_served)

#upr_9_5

class User():
	def __init__(self,first_name,last_name,age='',location='',ocupation=''):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + ' ' + last_name
		self.age = age
		self.location = location
		self.ocupation = ocupation
		self.login_attempts = 0

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

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

olyalya = User('olga','kartashova',location='murmansk')

User.increment_login_attempts(olyalya)
User.increment_login_attempts(olyalya)
User.increment_login_attempts(olyalya)
print(str(olyalya.login_attempts))
User.reset_login_attempts(olyalya)
print(str(olyalya.login_attempts))

#upr_9_6

class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print('The "' + self.restaurant_name.title() + '" is ' + self.cuisine_type + ' cuisine restaurant.')

	def open_restaurant(self):
		print(self.restaurant_name.title() + ' restaurant is opened.')

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type,*flavors):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors

	def add_to_flavors(self,*flavor):
		self.flavors += flavor

	def show_flavors_list(self):
		print('Our flavors list:')
		for flavor in self.flavors:
			print(flavor)

flavors=('avokado','mango','vanilla')
icecream = IceCreamStand('icy','icecream','avokado','mango','vanilla')
IceCreamStand.show_flavors_list(icecream)
IceCreamStand.add_to_flavors(icecream,'banana')
IceCreamStand.show_flavors_list(icecream)

#upr_9_7

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

class Admin(User):
	def __init__(self,first_name,last_name,*privileges):
		super().__init__(first_name,last_name)
		self.privileges = privileges

	def show_privileges(self):
		print(self.full_name + ':')
		for v in self.privileges:
			print(v)

admin_stew = Admin('Stew','Readly',
	'Разрешено добавлять сообщения',
	'Разрешено удалять пользователей',
	'Разрешено банить пользователей')

Admin.show_privileges(admin_stew)

#upr_9_8

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

admin_beka = Admin('beka','williams')
admin_beka.privileges.show_privileges()

#upr_9_9

class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometr_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()


class Battery():
	def __init__(self,battery_size=70):
		self.battery_size = battery_size

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = 'This car can go approximately ' + str(range)
		message += ' miles on a full charge.'
		print(message)

	def upgrade_battery(self):
		self.battery_size = 85 if self.battery_size != 85 else nothing

	def describe_battery(self):
		print('This car has a ' + str(self.battery_size) + '-kWh battery.')

class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()

my_wolf = ElectricCar('ww','polo',2015)
print(my_wolf.get_descriptive_name())
my_wolf.battery.get_range()
my_wolf.battery.upgrade_battery()
my_wolf.battery.get_range()


