import commonwords as cw


""" Класс для представления словаря """
class Glossary():
    def __init__(self,name,type):
        """ Модель словаря """
        self.name = name
        self.type = 'cw' or 'users'
        glossary_list.append(self.name)

    def choose_glossary(self):
        """ Выбрать словарь из списка доступных словарей """

    def show_glossaries(self):
        """ Показать список доступных словарей """
        print(glossary_list)

    def show_glossary_content(self):
        """ Показать список слов в словаре """
        for key,value in self.items():
            print(key.title() + ' - ' + value)

    def input_to_glossary(self):
        """ Ввод нового слова в словарь """
        word = 'Пожалуйста, напишите слово по-английски: '
        translation = 'Пожалуйста, добавьте перевод: '
        key = input(word)
        if key == 'выход':
            return False
        value = input(translation)
        massiv = (key,value)
        return massiv

    def add_to_glossary(self,key,value):
        """ Добавление слова в словарь """
        self[key] = value
        print('Есть! Слово "' + key + '" добавлено в словарь.')
        print(self)

    def add_another_to_glossary(self):
        """ Добавление ещё одного слова в словарь """

gloss = {}
glossary_list = []
my_gloss = Glossary('Мой словарь','users')
my_gloss2 = Glossary('1000 words','cw')
print(glossary_list)

#Glossary.add_to_glossary(gloss,'look','смотреть')
#Glossary.show_glossary_content(cw.cw1000_gloss)

""" Класс для представления пользователя """
class User():
    def __init__(self,name):
        """ Модель пользователя """
        self.name = name

    def greet_user(self):
        """ Приветствие """
        print('Приятно познакомиться, ' + self.name.title() + '!')

    def greet_user_again(self):
        """ Приветствие пользователя при следующем входе в программу """
        print('С возвращением, ' + self.name.title() + '!')


