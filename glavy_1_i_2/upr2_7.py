name = '  \tolga \nberchuk  '
#Ввела переменную а для облегчения кода при необходимости использовать кавыки вокруг строки
a = '"'
print(a+name+a)
print(a+name.lstrip()+a)
print(a+name.rstrip()+a)
print(a+name.strip()+a)