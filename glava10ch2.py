#3/10/2022 Попытка продолжить изучать Python, перехожу к исключениям

import json

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print('Give me two numbers and I will divide them. \n')
print("Enter 'q' to quit. ")


while True:
    first_number = input('First number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print('Letters could not be divided!')
    else:
        print(answer)
   
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('Sorry, the file ' + filename + ' does not exist.')
else:
    words = contents.split()
    num_words = len(words)
    print('This file contents ' + str(num_words) + ' words.')

title = 'Alice in Wonderland'
print(title.split())

def count_words(filename):
    '''Считает количество слов в тексте'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        missing_files = 'missing_files.txt'
        with open(missing_files, 'a') as f_obj:
            f_obj.write(filename + '\n')
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' contents ' + str(num_words) + ' words.')

filenames = ['alice.txt', 'text.txt', 'error.txt', 'test.txt', 'olya.txt']
for filename in filenames:
    count_words(filename)

#upr_10_6 + 10_7

print('Give me two numbers and I will add them.')
print('Enter q to quit. ')
while True:
    first_number = input('First number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        addition = int(first_number) + int(second_number)
    except ValueError:
        print ('Letters could not be added!')
    else:
        print(addition)

#upr_10_8

def read_file(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('The file ' + filename + ' does not exist.')
    else:
        print('The file ' + filename + ' text: ' + '\n')
        print(contents)

files = ['cats.txt', 'dogs.txt']
for filename in files:
    read_file(filename)

#upr_10_9

def read_file(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print('The file ' + filename + ' text: ' + '\n')
        print(contents)

files = ['cats.txt', 'dogs.txt']
for filename in files:
    read_file(filename)

#upr_10_10

def count_words(filename, word):
    try:
        with open(filename) as f_obj:
            text = f_obj.read()
    except FileNotFoundError:
        print('The file ' + filename + ' does not exist. ')
    else:
        words_count = text.lower().count(word)
        print('The file ' + filename + ' contains ' + str(words_count) + ' "' 
            + word + '" words.')

filenames = ['Mundita.txt', 'food of Gods.txt', 'Hameleon.txt']
for filename in filenames:
    count_words(filename, 'в')


files = ['Mundita.txt', 'food of Gods.txt', 'Hameleon.txt']
words = ['в', 'на', 'где']

combination = []
for file in files:
    for word in words:
        combination = [file, word]
        count_words(combination[0],combination[1])

# Начинаю изучать, как сохранять данные, введённые пользователем, 
# для дальнейшего использования

#upr_10_11

fav_number = input('What is your favourite number? ')
filename = 'fav_number.json'
with open(filename, 'w') as f_obj:
    json.dump(fav_number,f_obj)


with open(filename) as f_obj:
    number = json.load(f_obj)
print('I know your favorite number! It is ' + str(number) + '.')


#upr_10_12

try:
    filename = 'fav_number.json'
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    fav_number = input('What is your favourite number? ')
    with open(filename, 'w') as f_obj:
        json.dump(fav_number,f_obj)
else:
    print('I know your favorite number! It is ' + str(number) + '.')


#upr_10_13

def verify_username():
    """Проверяет актуальность имени пользователя"""
    username = get_stored_username()
    answer = input("Это ваше имя? (y/n)" + '\n' + username + ' ')
    if answer == 'n':
        get_new_username()

