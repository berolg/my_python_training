#17/03/2022 Начала главу 5 команда if

cars = ['audi','bmw','toyota','subaru']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print('\n')

book = 'little Prince'
if book.lower() == 'little prince':
	print('true')
else:
	print('false')

if book != 'Idiot':
    print('Hold "Idiot"!')

answer = 17
if answer == 17:
    print('Yes! You got it!')
if answer > 17:
    print('No, you need less.')
if answer < 17:
    print('No, you need more.')

answer = 26
answer1 = 21
if (answer >= 21) and (answer1 >= 21):
    print('You could buy alcohol')
else:
    print('You could not buy alcohol')

print(answer == 26)

answers = (26, 21)
print(26 in answers)
print(26 not in answers)
if 22 not in answers:
    print('Big brother is watching you')

#upr_5_1

book = 'Idiot'
print('Is the book "Idiot"? I predict True')
print(book == 'Idiot')
print('Is the book "Little Prince"? I predict False')
print(book == 'little Prince')

food = 'pizza'
print('Is the food "pizza"? I predict True')
print(food == 'pizza')
print('Is the food "ice-cream"? I predict False')
print(food == 'ice-cream')

olya = 'awake'
print('Is Olya sleeping? I predict False')
print(olya == 'sleeping')
print('Is Olya awake? I predict True')
print(olya == 'awake')

art = 'literature'
print('Is the art painting? I predict False')
print(art == 'painting')
print('Is the art literature? I predict True')
print(art == 'literature')

writing = 'oda'
print('Is the writing poetry? I predict False')
print(writing == 'poetry')
print('Is the writing oda? I predict True')
print(writing == 'oda')

#upr_5_2

book1 = 'Idiot'
book2 = 'little Prince'
print(book1 == book2)
print(book1 != book2)
print(book2.lower() == 'little prince')
number1 = 23
number2 = 13
print(number1 == number2)
print(number1 + number2 > 30)
print(number1 - number2 < 10)
print(number2 >= 10)
print(number1 + number2 != number2 - number1)
print(number1 * number2 <= 200)
if book1.lower() == 'idiot' and number1 <= 30:
    print('You win!')
if book2 == 'Idiot' or number2 > 10:
    print('You lose...')

books = [book1, book2]
if 'Idiot' in books:
    print('Yeah!')
if 'Great Gatsby' not in books:
    print('Nah.')

#upr_5_3

alien_color = 'yellow'
if alien_color == 'green':
    print('You got 5 points!')

alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points!')

#upr_5_4
alien_color = 'yellow'
if alien_color == 'green':
    print('You got 5 points!')
else:
    print('You got 10 points!')

alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points!')
else:
    print('You got 10 points!')

#upr_5_5

alien_color = 'yellow'
if alien_color == 'green':
    print('You got 5 points!')
elif alien_color == 'yellow':
    print('You got 10 points!')
else:
    print('You got 15 points!')

alien_color = 'green'
if alien_color == 'green':
    print('You got 5 points!')
elif alien_color == 'yellow':
    print('You got 10 points!')
else:
    print('You got 15 points!')

alien_color = 'red'
if alien_color == 'green':
    print('You got 5 points!')
elif alien_color == 'yellow':
    print('You got 10 points!')
else:
    print('You got 15 points!')

#upr_5_6

age = 3
if age < 2:
    print('baby')
elif age < 4:
    print('todler')
elif age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('old')

#upr_5_7

fruits = ['mangos','oranges','bananas']
if 'mangos' in fruits:
    print('I like mangos')
if 'apples' in fruits:
    print('I like apples')

favourite_fruits = fruits [:]
if 'mangos' in favourite_fruits:
    print('You really like mangos!')
if 'apples' in favourite_fruits:
    print('You really like apples!')
if 'bananas' in favourite_fruits:
    print('You really like bananas!')
if 'oranges' in favourite_fruits:
    print('You really like oranges!')
if 'plums' in favourite_fruits:
    print('You really like plums!')

#upr_5_8

names = ['admin','olya','vera','ilya','mihael','diana']
for name in names:
    if name == 'admin':
        print('Hello ' + name + ', would you like to see a status report?')
    else:
        print('Hello ' + name.title() + ', thank you for logging in again.')

#upr_5_9

names = []
if names:
    for name in names:
        if name == 'admin':
            print('Hello ' + name + ', would you like to see a status report?')
        else:
            print('Hello ' + name.title() + ', thank you for logging in again.')
else:
    print('We need to find some users!')

#upr_5_10

current_users = ['olya','vera','ilya','mihael','diana']
new_users = ['alla','anna','victor','elena','OLYA','miHael']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry, name "' + new_user + '" is not available, please choose another one.')
    else:
        print('Name "' + new_user +'" is available.')
#upr_5_11

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')