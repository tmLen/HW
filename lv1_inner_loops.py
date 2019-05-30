# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names_counter = {}
for student in students:
  names_counter[student['first_name']] = names_counter.get(student['first_name'], 0) + 1
for key, value in names_counter.items():
  print(f'{key}: {value}')
print()
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names_counter = {}
for student in students:
  names_counter[student['first_name']] = names_counter.get(student['first_name'], 0) + 1
max_value = 0
name = ''
for key, value in names_counter.items():
  if value > max_value:
    max_value = value
    name = key
print(f'Самое частое имя среди учеников: {name}', '\n')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
for index, students in enumerate(school_students):
  names_counter = {}
  for student in students:
    names_counter[student['first_name']] = names_counter.get(student['first_name'], 0) + 1
  max_value = 0
  name = ''
  for key, value in names_counter.items():
    if value > max_value:
      max_value = value
      name = key
  print(f'Самое частое имя в классе {index + 1}: {name}')
print()

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for group in school:
  boys = 0
  girls = 0
  for student in group['students']:
    if is_male[student['first_name']] == True:
      boys += 1
    else:
     girls += 1
  class_number = group['class']
  print(f'В классе {class_number} {girls} девочки и {boys} мальчика')
print()
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
more_boys = ''
more_girls = ''
max_boys_count = 0
max_girls_count = 0

for group in school:
  boys = 0
  girls = 0
  for student in group['students']:
    if is_male[student['first_name']] == True:
      boys += 1
    else:
     girls += 1
  if boys > max_boys_count:
    max_boys_count = boys
    more_boys = group['class']
  if girls > max_girls_count:
    max_girls_count = girls
    more_girls = group['class']
print(f'Больше всего мальчиков в классе {more_boys}')
print(f'Больше всего девочек в классе {more_girls}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a