# Задание 1

print('Задание 1')

year = int(input('Введите год выпуска велосипеда:'))
speed = int(input('Введите количество скоростей:'))

if year >= 2018 and speed >= 24:
  print('Велосипед подходит!')
else:
  print('Велосипед не подходит!')

# Задание 2

print('Задание 2')

point = int(input('Сколько баллов набрал Илья? '))
medal = int(input('Есть ли золотая медаль? (1 — да, 0 — нет) '))

if point > 280 and medal == 1:
  print('Илья поступил!')
else:
  print('Илья не поступил!')

# Задание 3

print('Задание 3')

temperature = int(input('Введите показатель температуры:'))

if temperature < 0 or temperature > 100:
  print('Предупреждение!')
else:
  print('Всё хорошо!')