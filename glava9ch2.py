from uprglava9 import Restaurant,Admin
from upr9_12plus import Admin,Privileges
from collections import OrderedDict

#upr_9_10

makaka = Restaurant('makaka','indian')
Restaurant.describe_restaurant(makaka)

#upr_9_11

admin_q = Admin('q','q')
admin_q.privileges.show_privileges()

#upr_9_12

admin_p = Admin('p','p')
admin_p.privileges.show_privileges()

#upr_9_13

definitions = OrderedDict()
definitions = {
    'конкатенация' : 'объединение строк', 
    'список' : 'набор элементов, следующих в определённом порядке', 
    'кортеж' : 'неизменяемый список',
    'словарь' : 'структура данных, предназначенная для объединения взаимосвязанной информации',
    'строка' : 'простая последовательность символов',
    'values()' : 'метод для получения значений словаря без ключей',
    'keys()' : 'метод для получения ключей словаря без значений',
    'условие' : 'выражение, резултатом которого является логическая истина (True) или логическая ложь (False)', 
    'срез' : 'подмножество элементов списка', 
    'len()' : 'метод для определения длины списка',
    }

for k,v in definitions.items():
	print(k.title() + ' - ' + v + '.')

#upr_9_14

from random import randint

x = randint(1,6)
print(x)

class Die():
	def __init__(self,sides=6):
		self.sides = sides
	
	def roll_die(self):
		roll = randint(1,self.sides)
		print('Кубик брошен: ' + str(roll))

default_kube = Die()
kube_10 = Die(10)
kube_20 = Die(20)

kubes = (default_kube,kube_10,kube_20)
for kube in kubes:
	x = 0
	while x != 10:
		Die.roll_die(kube)
		x += 1
	print('\n')

#upr_9_15

#done
