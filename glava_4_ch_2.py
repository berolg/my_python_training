#срезы списка
domestiс_animals = ['dogs','cats','pigs','chikens','cows','fish']
print(domestiс_animals[3:6])
print(domestiс_animals[:3])
print(domestiс_animals[2:])

print('\nI have domestic animals:')
for animal in domestiс_animals[:3]:
	print(animal.title())

#копия списка
domestiс_animals_copy = domestiс_animals[:]
print(domestiс_animals_copy)

#upr_4_10

print('The first three items in the list are:')
print(domestiс_animals[:3])
print('Three items in the middle of the list are:')
print(domestiс_animals[2:5])
print('The lfst three items in the list are:')
print(domestiс_animals[-3:])

#upr_4_11

pizzas = ['margarita','4 seniors','cheesy']
friend_pizzas = pizzas[:]

pizzas.append('romano')
friend_pizzas.append('venice')

print('My favourite pizzas are:')
for pizza in pizzas:
	print(pizza)

print('\nMy friend favourite pizzas are:')
for pizza in friend_pizzas:
	print(pizza)

#upr_4_12

my_foods = ['carot cake', 'pizza', 'falafel']
friend_foods = my_foods[:]

print('My favourite foods are:')
for food in my_foods:
	print(food)

print('My friend favourite foods are:')
for food in friend_foods:
	print(food)

# кортежи - неизменяемые списки

kortej = (2,0,4)
for kort in kortej:
	print(kort)

#upr_4_13

shved_stol = ('sup kurinuy','pelmeni','borsch','salat cesar','shashlyk')
print('Shvedskiy stol:')
for bludo in shved_stol:
	print(bludo)
print('Menu shvedskogo stola izmenilos:')
shved_stol = ('sup harcho','kuritsa','borsch','salat cesar','shashlyk')
for bludo in shved_stol:
	print(bludo)
