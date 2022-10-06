#13/03/22 начала изучать списки(массивы) Глава 3

names = ['olya','ilya','vera']
print(names)

print(names[0])
print(names[-1])

#upr_3_1

names = ['ilya','mihail','vera']
print(names[0].title())
print(names[1].title())
print(names[2].title())

#upr_3_2

names = ['ilya','mihail','vera']
message = ' is my friend.'
print(names[0].title()+message)
print(names[1].title()+message)
print(names[2].title()+message)

#upr_3_3

animes =['one piece','gintama','ace of diamond','bakuman']
message ='I really like the anime named '
dot ='.'
print(message+animes[0].title()+dot)
print(message+animes[-1].title()+dot)
print(message+animes[1].title()+dot)
print(message+animes[2].title()+dot)

#изменение элементов списка
animes =['one piece','gintama','ace of diamond','bakuman']
print(animes)

animes[0]='death note'
print(animes)

# добавление элементов в список
animes =['one piece','gintama','ace of diamond','bakuman']
animes.append('d.grey-man')
print(animes)

# работа с пустым списком
animes = []
animes.append('one piece')
print(animes)
animes.append('d.grey-man')
print(animes)

# вставка элемента списка в определенное место
animes =['one piece','gintama','ace of diamond','bakuman']
animes.insert(2,'d.grey-man')
print(animes)

#удаление элемента списка
# del удаляет элемент навсегда, с ним больше нельзя работать
del animes[2]
print(animes)

# pop удаляет элемент только из списка, но с ним дальше можно работать
popped_anime = animes.pop()
print(animes)
print(popped_anime)
message = 'The last but not least in my favourite anime list is ' + popped_anime.title() + dot
print(message)

popped_anime = animes.pop(0)
message = 'The first in my animes top is ' + popped_anime.title()
print(message)
print(animes)

# remove удаляет элемент, чей индекс неизвестен, но известно значение (удаляет только первое вхождение заданного значения, для удаления всех значений нужно написать цикл)
# чтобы работать с удаленным элементом дальше, нужно сохранить его в переменной перед удалением
animes =['one piece','gintama','ace of diamond','bakuman']
animes.remove('gintama')
print(animes)

animes =['one piece','gintama','ace of diamond','bakuman']
meme = 'gintama'
animes.remove(meme)
print(animes)
message = meme.title()+" was removed because it's a meme."
print(message)

#upr_3_4

gosti=['Kuramochi Youichi','myka Nina', 'Rollo May']
invitation = ', you are invited tо my dinner!'
print(gosti[0]+invitation)
print(gosti[1].title()+invitation)
print(gosti[2]+invitation)

#upr_3_5

gosti=['Kuramochi Youichi','myka Nina', 'Rollo May']
print(gosti[1])
gosti[1]='Alexander Dumas'
print(gosti)
invitation = ', you are invited tо my dinner!'
print(gosti[0]+invitation)
print(gosti[1]+invitation)
print(gosti[2]+invitation)

#upr_3_6

gosti=['Kuramochi Youichi','Alexander Dumas', 'Rollo May']
message = 'I bought a big new dinner table, we have space for some more guests!'
print(message)
gosti.insert(0,'Vera Shambur')
gosti.insert(2,'Mihail Nikiforov')
gosti.append('Ilya Cheburov')
print(gosti)
print(gosti[0]+invitation)
print(gosti[1]+invitation)
print(gosti[2]+invitation)
print(gosti[3]+invitation)
print(gosti[4]+invitation)
print(gosti[5]+invitation)

#upr_3_7
gosti = ['Vera Shambur', 'Kuramochi Youichi', 'Mihail Nikiforov', 'Alexander Dumas', 'Rollo May', 'Ilya Cheburov']
message = 'Unfortunately, the table will be delivered on two weeks, I have places for only two guests!'
print(message)
popped_guest = gosti.pop()
message = popped_guest+', I am sorry to announce your invitation is cancelled.'
print(message)
popped_guest = gosti.pop()
message = popped_guest+', I am sorry to announce your invitation is cancelled.'
print(message)
popped_guest = gosti.pop()
message = popped_guest+', I am sorry to announce your invitation is cancelled.'
print(message)
popped_guest = gosti.pop()
message = popped_guest+', I am sorry to announce your invitation is cancelled.'
print(message)
invitation = ', your invitation is valid!'
print(gosti)
print(gosti[0]+invitation)
print(gosti[1]+invitation)

del gosti[0]
del gosti[0]
print(gosti)

# сортировка списка
# sort для постоянной сортировки 
# sorted для временной сортировки

animes =['one piece','gintama','ace of diamond','bakuman']
animes.sort()
print(animes)
animes.sort(reverse=True)
print(animes)

print ('\nHere is the origina list:')
print(animes)
print('\nHere is the sorted list:')
print(sorted(animes))
print('\nAnd here is the original list again:')
print(animes)

# обратный порядок в списке
animes =['one piece','gintama','ace of diamond','bakuman']
animes.reverse()
print(animes)

animes = ['one piece','gintama']
print(len(animes))

#upr_3_8

countries =['Australia','France','Slovenia','Great Britain']
print('\n')
print(countries)

print(sorted(countries))
print(countries)
print(sorted(countries,reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

#upr_3_9

gosti=['Kuramochi Youichi','Alexander Dumas', 'Rollo May']
message = 'I bought a big new dinner table, we have space for some more guests!'
print(message)
gosti.insert(0,'Vera Shambur')
gosti.insert(2,'Mihail Nikiforov')
gosti.append('Ilya Cheburov')
print(gosti)
print(gosti[0]+invitation)
print(gosti[1]+invitation)
print(gosti[2]+invitation)
print(gosti[3]+invitation)
print(gosti[4]+invitation)
print(gosti[5]+invitation)

print('\n')
invited_guests = len(gosti)
message = str(invited_guests) +' guests are invited to the dinner.'
print(message)



