# 20/03/2022 начинаю изучать словари

slova = {'dog':'собака', 'god':'Бог'}
print(slova['god'])

print(slova)
slova['soul'] = 'душа'
slova['cool'] = 'крутой'
print(slova)

del slova['cool']
print(slova)

print('Soul in english means "' +
	slova['soul'] + '".')

slova = {
	'dog': 'собака', 
	'god': 'Бог', 
	'soul': 'душа'
	}

print(slova)

#upr_6_1

me = { 'first_name' : 'olya', 'last_name' : 'berchuk', 'age' : 26, 
    'city' : 'Saint-Petersburg'}
print(me['first_name'].title())
print(me['last_name'].title())
print(me['age'])
print(me['city'])

#upr_6_2

favourite_numbers = {'sara' : 5, 'olya' : 16, 'vera' : 20, 'mihael' : 13, 'ilya' : 15}
print("Sara's favourite number is " + str(favourite_numbers['sara']) + '.')
print("Olya's favourite number is " + str(favourite_numbers['olya']) + '.')
print("Vera's favourite number is " + str(favourite_numbers['vera']) + '.')
print("Mihael's favourite number is " + str(favourite_numbers['mihael']) + '.')
print("Ilya's favourite number is " + str(favourite_numbers['ilya']) + '.')

#upr_6_3 Словарь глоссарий

definitions = {
    'конкатенация' : 'объединение строк', 
    'список' : 'набор элементов, следующих в определённом порядке', 
    'кортеж' : 'неизменяемый список',
    'словарь' : 'структура данных, предназначенная для объединения взаимосвязанной информации',
    'строка' : 'простая последовательность символов'
    }
print(definitions.keys())
for definition in definitions.keys():
    print(definition.title() + ' - ' + definitions[definition] + '.')
    print('\n')

for word, definition in definitions.items():
    print('\nWord: ' + word)
    print('Definition: ' + definition)

print(sorted(definitions.keys()))

print(definitions.values())

definitions = {
    'конкатенация' : 'объединение строк', 
    'список' : 'набор элементов, следующих в определённом порядке', 
    'кортеж' : 'неизменяемый список',
    'словарь' : 'структура данных, предназначенная для объединения взаимосвязанной информации',
    'строка' : 'простая последовательность символов',
    'кортh' : 'неизменяемый список',
    'кортb' : 'неизменяемый спислок'
    }
for word, definition in definitions.items():
    print('\nWord: ' + word)
    print('Definition: ' + definition)
print(definitions.keys())
print(definitions.values())

print(set(definitions.values()))

#upr_6_4

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
print(definitions.keys())
for definition in definitions.keys():
    print(definition.title() + ' - ' + definitions[definition] + '.')
    print('\n')

#upr_6_5

rivers = {'Russia' : 'volga', 'transnistria' : 'nistru', 'egypt' : 'nile'}
for country, river in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + '.')
for river in rivers.values():
    print(river.title())
for country in rivers.keys():
    print(country.title())

#upr_6_6

favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
    }
people = ['olya', 'sarah', 'phil', 'ilya']
for name in people:
    if name in favourite_languages.keys():
        print(name.title() + ', thank you for filling the poll!')
    else:
        print(name.title() + ', would you fill the poll?')

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

user_1 = {
    'name' : 'olya',
    'age' : 26,
    'education' : ['school', 'university']
    }

user_2 = {
    'name' : 'ilya',
    'age' : 30,
    'education' : ['school', 'college', 'university']
    }

users = [user_1, user_2]

#upr_6_7

me = { 'first_name' : 'olya', 'last_name' : 'berchuk', 'age' : 26, 
    'city' : 'Saint-Petersburg'}
ilya = {'first_name' : 'ilya', 'last_name' : 'chevurov', 'age' : 30, 
    'city' : 'Saint-Petersburg'}
vera = {'first_name' : 'vera', 'last_name' : 'shambur', 'age' : 25, 
    'city' : 'Moscow'}
people = [me, ilya, vera]

for human in people:
    print(human['first_name'].title())
    print(human['last_name'].title())
    print(human['age'])
    print(human['city'].title())

#upr_6_8

yakubashka = { 'pet' : 'cat', 'owner' : 'diana'}
krasotka = { 'pet' : 'cat', 'owner' : 'anna'}
rem = { 'pet' : 'dog', 'owner' : 'alla'}

pets = [yakubashka, krasotka, rem]

for pet in pets:
    print(pet['pet'])
    print(pet['owner'].title())

#upr_6_9

favorite_places = {'olya':['ogurtsy','sofa','auchan'], 
    'ilya':['europa iv','home','mama na dache'], 
    'diana':['twitter','sofa','kazansky sobor']
    }
for people, places in favorite_places.items():
    print(people.title() + "'s favourite places are:")
    for place in places:
        if place == 'europa iv':
            print(place.upper())
        elif place == 'mama na dache':
            print('Mama na dache')
        elif place == 'kazansky sobor':
            print('Kazansky sobor')
        else:
            print(place.title())

#upr_6_10

favourite_numbers = {'sara' : [5,3,6], 'olya' : [16], 'vera' : [20,25], 
    'mihael' : [666,13], 'ilya' : [15]}
for name, numbers in favourite_numbers.items():
    print(name.title())
    for number in numbers:
        print(str(number))

#upr_6_11

cities = {
    'moscow':{
        'country' : 'russia', 
        'population' : '20 millions', 
        'fact' : 'Moscow is the city of possibilities'},
    'tokyo' : {
        'country' : 'japan',
        'population' : '37 millions',
        'fact' : 'Tokyo is the largest metropolitan in the world'},
    'melbourne' : {
        'country' : 'australia',
        'population' : '5 millions',
        'fact' : "Melbourne is considered Australia's unofficial sporting capital"}
    }

for city, city_info in cities.items():
    print('\n')
    print(city.title() + ':')
    print('Country: ' + city_info['country'].title())
    print('Population: ' + city_info['population'])
    print('Fact: ' + city_info['fact'])








