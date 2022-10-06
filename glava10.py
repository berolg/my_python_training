# Начинаю изучать файлы и исключения 23/04/2022

with open ('text.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('commonwords.py') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('commonwords.py') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

with open('commonwords.py') as file_object:
    lines = file_object.readlines()
gloss_string = ''
for line in lines:
    gloss_string += line.strip()

print(gloss_string)

# Находит в словаре строки с символом слэша и сохраняет их в списке words
file_name = 'commonwords.py'
with open(file_name) as file_object:
    lines = file_object.readlines()
words = ''
for line in lines:
    flag = '/'
    if flag in line:
        words += line

print(words)

#upr_10_1

file_path = 'learning_python.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

print('\n')

with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

txt = ''
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        txt += line
print('\n')
print(txt)

#upr_10_2

with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        v = line.replace('Python','C')
        print(v)

file = 'writing_file.txt'
with open(file,'w') as file_object:
    file_object.write('I love writing.\n')
    file_object.write('I have written a novel.\n')

with open(file,'a') as file_object:
    file_object.write('In my novel the man has died in fire.\n')
    file_object.write('After death his soul cannot reach the other side because his girlfriend could not suffer his death.\n')

#upr_10_3

file = 'guest.txt'
with open(file,'w') as file_object:
    name = input('Hello! What is your name? ')
    file_object.write(name)
    print('Nice to meet you, ' + name.title() + '!')

#upr_10_4

file = 'guest_book.txt'

name = ''
while name != 'q':
    with open(file,'a') as file_object:
        name = input('Hello! What is your name? ')
        if name == 'q':
            break
        else:
            file_object.write(name + '\n')
            print('Nice to meet you, ' + name.title() + '!')


#upr_10_5

answer = ''
while answer != 'q':
    with open('upr10_5.txt','a') as file_object:
        answer = input('Почему тебе нравится программировать? ')
        if answer == 'q':
            break
        else:
            file_object.write(answer + '\n')


