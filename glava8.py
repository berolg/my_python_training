# 23/03/2022 Начинаю изучать функции

#upr_8_1

def display_message():
    print('Тема этой главы - функции!')

display_message()

#upr_8_2

def favorite_book(title):
    print('One of my favorite books is ' + title.title() + '.')

favorite_book('War and peace')

#upr_8_3

def make_shirt(size,text):
    print("Shirt's size is " + size + '.')
    print('The following text is written on the shirt:"' + text + '".')

make_shirt('M','I am learning Python')
make_shirt(size = 'L',text = 'My favorite activity is sleeping')

#upr_8_4

def make_shirt(size = 'L',text = 'I love Python'):
    print("Shirt's size is " + size + '.')
    print('The following text is written on the shirt:"' + text + '".')

make_shirt()
make_shirt('M','I am learning Python')

#upr_8_5

def describe_city(city, country='Russia'):
    """Эта функция описывает город"""
    print(city.title() + ' is in ' + country.title() + '.')

describe_city('Moscow')
describe_city('new york', 'unites states')
describe_city('podoima','transnistria')

def get_formated_name(first_name, last_name):
    """Эта функция объединяет имя и фамилию в полное имя"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formated_name('olga','berchuk'))

def get_formated_name_middle(first_name, last_name, middle_name=''):
    """Эта функция выводит ФИО с отчеством, если оно есть"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

name = get_formated_name_middle('olga','berchuk')
print(name)

name = get_formated_name_middle('olga','berchuk','grigorevna')
print(name)

def person_build(first_name,last_name,age = ''):
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

print(person_build('olga','berchuk',26))
print(person_build('vera','shambur'))

#upr_8_6

def city_country(city,country,population=''):
    if population:
        full_city_country = city + ', ' + country + ' - ' + str(population)
    else:
        full_city_country = city + ', ' + country
    return full_city_country.title()

#while True:
#    city = input('City: ')
#    if city == 'q':
#        break
#    country = input('Country: ')
#    if country == 'q':
#        break
#    print(city_country(city,country))

#upr_8_7

def make_album(artist,album_name,songs = ''):
    album = {'artist':artist, 'album_name':album_name}
    if songs:
        album['songs'] = songs
    return album
print(make_album('U2','Young'))
print(make_album('Brothers','Porn'))
print(make_album('Korn','Darkness'))
print(make_album('Beatles','Yesterday',12))

#upr_8_8

def make_album(artist,album_name,songs = ''):
    album = {'artist':artist, 'album_name':album_name}
    if songs:
        album['songs'] = songs
    return album

#while True:
#    artist = input('Artist: ')
#    if artist == 'q':
#        break
#    album_name = input('Album name: ')
#    if album_name == 'q':
#        break
#    print(make_album(artist,album_name))

#upr_8_9

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['harry','gale','mary','peter']
#show_magicians(magicians)

#upr_8_10

magicians = ['harry','gale','mary','peter']

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for idx, magician in enumerate(magicians):
        magicians[idx] = 'Great ' + magician

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

#upr_8_11

magicians = ['harry','gale','mary','peter']
great = []

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for idx, magician in enumerate(magicians):
        magicians[idx] = 'Great ' + magician
        great.append(magicians[idx])

show_magicians(magicians)
make_great(magicians[:])
show_magicians(great)

def make_pizza(*topings):
    print('\nMaking a pizza with the following topings:')
    for toping in topings:
        print('- ' + toping)

make_pizza('cheese','plums','avokado')
make_pizza('eggs')

def make_pizza(size,*topings):
    print('\nMaking a ' + str(size) + '-inch pizza with the following topings:')
    for toping in topings:
        print('- ' + toping)

make_pizza(12,'cheese','plums','avokado')
make_pizza(26,'eggs')

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('olga','berchuk',location = 'russia',ocupation = 'writer')
print(user_profile)

#upr_8_12

def make_sandwich(*topings):
    print('\nMaking a sandwich with following topings: ')
    for toping in topings:
        print('- ' + toping)

make_sandwich('eggs','banana','cheese','avokado')
make_sandwich('apple','chiken')
make_sandwich('eggs','fish','ketchup')

#upr_8_13

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('olga','berchuk',location = 'russia',ocupation = 'writer',
    hobby = 'python')
print(user_profile)

#upr_8_14

def car_profile(manufacturer,model,**car_info):
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key,value in car_info.items():
        profile[key] = value
    return profile

car = car_profile('honda','civic',color = 'blue', cabine = 'leather')
print(car)
car = car_profile('kia','rio',type = 'crossover',cabine = 'plastic')
print(car)

