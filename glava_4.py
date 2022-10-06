#13/03/22 Начинаю изучать циклы for
# строка, следующая за for, должна быть с отступом, иначе выскочит ошибка
names = ['olya','ilya','vera']
for name in names:
	print(name.title()+' - what a beautifull name!')
	print('I wish my name was '+name.title()+'.\n')

#upr_4_1

pizzas = ['margarita','4 seniors','cheesy']
for pizza in pizzas:
	print('I like '+pizza+' pizza.')
print('I really love pizza!')

#upr_4_2

domestiс_animals = ['dogs','cats','pigs','chikens']

for domestiс_animal in domestiс_animals:
	print(domestiс_animal.title()+' are cute.')
print('\nAny of these animals are domestic.')

for value in range(1,6):
	print(value)
print(list(range(1,6)))

print(list(range(1,6,2)))

kvadrats=[]
for value in range(1,6,2):
	kvadrat = value**2
	kvadrats.append(kvadrat)
print(kvadrats)

print(sum(kvadrats))
print(min(kvadrats))
print(max(kvadrats))

kvadrats =[value**2 for value in range(1,6,2)]
print(kvadrats)

#upr_4_3

for upr in range(1,21):
	print(upr)

#upr_4_4 i 4_5

million =[]
for upr in range(1,1000001):
	print(upr)
	million.append(upr)
print(min(million))
print(max(million))
print(sum(million))

#upr_4_6

nechet=[]
for upr in range(1,20,2):
	nechet.append(upr)
print(nechet)

#upr_4_7

troiki = []
for upr in range(3,30,3):
	troiki.append(upr)
print(troiki)

#upr_4_8

kuby = []
for upr in range(1,11):
	kub = upr**3
	kuby.append(kub)
print(kuby)

#upr_4_9

kuby=[upr**3 for upr in range(1,11)]
print(kuby)