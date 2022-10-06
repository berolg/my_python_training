# 06/10/2022 Начала изучать тестирование

import unittest

class NamesTestCase(unittest.TestCase):
	"""Тесты для имен """
	def test_first_last_name(self):
		"""Работают ли правильно имена без middle?"""
		formatted_name = get_formatted_name('olya','berchuk')
		self.assertEqual(formatted_name, 'Olya Berchuk')

	def test_first_last_middle_name(self):
		"""Работают ли правильно имена с middle?"""
		formatted_name = get_formatted_name('olya','berchuk','molya')
		self.assertEqual(formatted_name,'Olya Molya Berchuk')

def get_formatted_name(first,last,middle=''):
	""" Строит полное отформатированное имя """
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

print('Enter q at anytime to quit. ')
while True:
	first = input('\n Please give me a first name: ')
	if first == 'q':
		break
	last = input('Please give me a last name: ')
	if last == 'q':
		break
	formatted_name = get_formatted_name(first, last)
	print('\tNeatly formatted name: ' + formatted_name + '.')

#upr_11_1_&_11_2

from glava8 import city_country

class CitiesTestCase(unittest.TestCase):
	"""Выводится ли правильно Сантьяго, Чили?"""
	def test_city_country(self):
		result = city_country('moscow','russia')
		self.assertEqual(result, 'Moscow, Russia')

	def test_city_country_population(self):
		"""Выводится ли правильно город, страна с населением?"""
		result = city_country('moscow','russia',20000000)
		self.assertEqual(result, 'Moscow, Russia - 20000000')

class AnonymousSurvey():
	"""Сбор анонимных ответов на вопросы"""
	def __init__(self,question):
		"""Сохраняет вопрос и готовится к сохранению ответа"""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Выводит вопрос"""
		print(self.question)

	def store_response(self,new_response):
		"""Сохраняет один ответ на вопрос"""
		self.responses.append(new_response)

	def show_results(self):
		"""Выводит все полученные результаты"""
		print('Survey results: ')
		for response in self.responses:
			print('- ' + response)

question = 'How old are you?'
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print('Enter q at anytime to quit. \n')
while True:
	response = input('Years: ')
	if response == 'q':
		break
	my_survey.store_response(response)

my_survey.show_results()

class SurveyTestCase(unittest.TestCase):
	"""Тесты для анонимного опроса"""
	def setUp(self):
		"""Создание экземпляра опроса и ответов для всех методов"""
		question = 'How old are you?'
		self.my_survey = AnonymousSurvey(question)
		self.responses = [20,21,22]

	def test_store_single_response(self):
		"""Проверяет, что один ответ сохраняется правильно"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_response(self):
		"""Проверяет, что три ответа сохраняется правильно"""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

#upr_11_3

class Employee():
	"""Класс работника"""
	def __init__(self,firstname,lastname,salary):
		self.firstname = firstname
		self.lastname = lastname
		self.salary = salary

	def give_raise(self,rise = 5000):
		self.rise = rise
		self.salary += rise
		print(self.firstname.title() + ' ' + self.lastname.title() 
			+ "'s salary now is " + str(self.salary) + '.')

olya = Employee('olya','berchuk',20000)
olya.give_raise(10000)
osal = olya.salary
print(osal)

class EmployeeTestCase(unittest.TestCase):
	"""Тесты для проверки класса Работник"""
	def setUp(self):
		"""Создает экземпляр класса работник и сохраняет величину 
		прибавки по умолчанию"""
		self.employee_info = ['olya','berchuk',20000]
		self.my_employee = Employee(self.employee_info[0],
			self.employee_info[1],self.employee_info[2])
		self.default_raise = 5000

	def test_give_default_raise(self):
		"""Проверка прибавки по умолчанию"""
		self.my_employee.give_raise()
		self.assertEqual(self.employee_info[2] + self.default_raise, 
			self.my_employee.salary)

	def test_give_customized_raise(self):
		custom_raise = 10000
		self.my_employee.give_raise(custom_raise)
		self.assertEqual(self.employee_info[2] + custom_raise, self.my_employee.salary)

unittest.main()








