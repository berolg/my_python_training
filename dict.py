# 20/03/2022
# Хочу создать словарь для заучивания английских слов. 
# С возможностью добавлять новые слова, заучивать в обе стороны 
# (давать перевод на английское слово и давать английское слово на перевод), 
# а также с возможностью отслеживать свой прогресс.

# Что ещё хочу добавить:
# - если у слова несколько значений, любое из них должно учитываться, как верное
# - чтобы при неверном ответе показывалось, какой ответ является верным
# - чтобы слова сохранялись в словаре при следующем запуске
# - чтобы приложение помнило имя пользователя
# - чтобы можно было создавать несколько профилей для разных пользователей с разными словарями
# - чтобы пользователи могли делиться словарями друг с другом
# - чтобы можно было добавлять разные словари (по категориям, например, словарь 100 самых 
# используемых слов, кухонный словарь и т.д.)
# - чтобы можно было отслеживать прогресс
# - чтобы можно было отслеживать прогресс во времени
# - чтобы вместо команд были кнопки
# - чтобы при вводе в словарь, программа проверяла, на каком языке ввод, 
# и выдавала предупреждение, если язык неправильный

import commonwords
import json

glossary = {'dog': 'собака', 'god': 'Бог', 'soul': 'душа', 'cool': 'крутой'}

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Получает новое имя пользователя"""
    username = input('Привет, я приложениe для изучения слов! Как вас зовут? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def verify_username():
    """Проверяет актуальность имени пользователя"""
    username = get_stored_username()
    answer = input("Это ваше имя? (y/n)" + '\n' + username + ' ')
    if answer == 'n':
        get_new_username()

def greet_user():
    """ Приветствие """
    verify_username()
    username = get_stored_username()
    if username:
        print('С возвращением, ' + username.title() + '!')
    else:
        username = get_new_username()
        print('Приятно познакомиться, ' + username.title() + '!')
        print('\n')
        spravka(True)
        
def spravka(tumblr):
    """ Справка """
    faq = '\nУ вас есть много возможностей!\nВы можете добавлять новые слова в словарь, ' \
    + 'заучивать карточки как с английского на русский, так и наоборот.' + \
    '\nСкоро вам будет доступно отслеживание прогресса.' + \
    '\nВведите команду "добавить", чтобы добавить новые слова в словарь.' +\
    '\nЧтобы начать изучать слова, введите команду "карточки".' + \
    '\nВведите команду "выход" в любой момент, чтобы закончить работу с приложением.' +\
    '\nВведите команду "справка", чтобы вернуться к списку команд.'
    if tumblr:
        answer = input(username.title() + 
            ', рассказать вам, что вы можете делать в этом приложении? (да/нет) ')
        if answer == 'да':
            print(faq)
    else:
        print(faq)


def vvod():
    """ Ввод слов и перевода для добавления в словарь """
    word = 'Пожалуйста, напишите слово по-английски: '
    translation = 'Пожалуйста, добавьте перевод: '
    word_key = input(word)
    if word_key == 'выход':
        return False
    word_value = input(translation)
    massiv = (word_key,word_value)
    return massiv

def add(word_key,word_value):
    """ Добавление нового слова в словарь """
    glossary[word_key] = word_value
    print('Есть! Слово "' + word_key + '" добавлено в словарь.')
    print(glossary)
    
def add_plus():
    """ Добавление дополнительного слова в словарь """
    print('\nДобавить ещё одно слово? (да/нет) ')
    add_another = input(' ')
    return True if add_another == 'да' else False

def learning(kartochki):
    """ Заучивание карточек """
    for key,value in glossary.items():
        if kartochki == 'слова':
            print('\nЗдесь вы можете изучать перевод английских слов.')
            print('Введите перевод:')
        else:
            print('\nЗдесь вы можете переводить слова на английский.')
            print('Введите слово по-английски:')
        answer = input(key if kartochki == 'слова' else value + ': ')    
        if answer == 'выход':
            break
        if answer == glossary[key] if kartochki == 'слова' else key:
            print('Верно!')
        else:
            print('Нет :(')

greet_user()
        
while True:
    komanda = input('\nКоманда: ')

    if komanda == 'выход':
        break
    elif komanda == 'справка':
        spravka(False)
    elif komanda == 'добавить':
        print('Здесь вы можете добавить новые слова в словарь.\n')
        while True:
            value = vvod()
            if value == False:
                break
            if value[0] == 'выход' or value[1] == 'выход':
                break
            add(value[0],value[1])
            value = add_plus()
            if value == False:
                break

    elif komanda == 'карточки':
        print('Вы хотите получать от приложения карточки с английскими словами или переводом? (слова/перевод) ')
        kartochki = input(' ')
        
        if kartochki == 'выход':
            break
            
        learning(kartochki)

print('Всё!')