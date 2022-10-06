# 20/03/2022 начинаю изучать циклы while и ввод данных

slova = {'dog': 'собака', 'god': 'Бог', 'soul': 'душа', 'cool': 'крутой'}

message = input('What is your name? ')
print('Hello, ' + message.title() + '!')

word = 'Please add the word in english: '
translation = 'Please add the translation: '
active = True
while active:
	word_key = input(word)
	if word_key == 'quit':
		active = False
	else:
		word_value = input(translation)
		slova[word_key] = word_value
print('The words have been added to base:')
print(slova)

#upr_7_1

car = input('Which car do you want to rent? ')
print('Let me see if I could find a ' + car.title() + ' for you.')

#upr_7_2

table = input('How many guests do you need a table for? ')
table = int(table)
if table >= 8:
	print('Sorry, you need to wait for a big table.')
else:
	print('Your table is ready.')

#upr_7_3

number = input('Enter a number and I will tell you if it is even divisible by 10: ')
number = int(number)
if number % 10 == 0:
	print('This number is even divisible by 10.')
else:
	print('This number is not even divisible by 10.')

#upr_7_4

while True:
	toping = input('Choose toping for your pizza: ')
	if toping == 'quit':
		break
	else:
		print(toping.title() + ' is added to your pizza')

#upr_7_5

age = input('How old are you? ')
age = int(age)
if age < 3:
	price = 0
elif age < 12:
	price = 10
else:
	price = 15
print('Your ticket cost is ' + str(price) +'$.')

#upr_7_6

active = True
while active:
	age = input('How old are you? ')
	if age == 'quit':
		break
		active = False
	age = int(age)
	if age < 3:
		price = 0
	elif age < 12:
		price = 10
	else:
		price = 15
	print('Your ticket cost is ' + str(price) +'$.')

#upr_7_8

sandwich_orders = ['tuna sandwich', 'chiken sandwich', 'vegan sandwich']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print('I made your ' + current_sandwich)
	finished_sandwiches.append(current_sandwich)
print('These sandwiches are finished:')
for sandwich in finished_sandwiches:	
	print(sandwich)

#upr_7_9

sandwich_orders = ['pastrami sandwich','tuna sandwich', 'pastrami sandwich', 
	'chiken sandwich', 'pastrami sandwich', 'vegan sandwich']
finished_sandwiches = []

print('Sorry, we do not have pastrami.')
while 'pastrami sandwich' in sandwich_orders:
	sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print('I made your ' + current_sandwich)
	finished_sandwiches.append(current_sandwich)
print('These sandwiches are finished:')
for sandwich in finished_sandwiches:	
	print(sandwich)

#upr_7_10

responses = {}
poll_active = True
while poll_active:
	name = input('What is your name? ')
	vacation = input('Where would you like to go to your vacation? ')
	responses[name] = vacation
	quit = input('Would you like another person to answer? (y/n) ')
	if quit == 'y':
		continue
	else:
		break
print('\nPoll results:')
for name, response in responses.items():
	print(name.title() + ' want to go to ' + response.title() + '.')

