#1 Фильтрация списка по четным элементам
numbers = [i for i in range(1, 12)]

filter_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f'Фильтрация списка по четным элементам {filter_numbers}')

#2 Возврат квадрата значений списка
map_numbers = list(map(lambda x: x ** 2, numbers))

print(f'Возврат квадрата значений списка {map_numbers}')

#3 В методе sorted есть встроенная функция len, если ее передать в key, она отсортирует по длине значения
fruits = ['apple', 'banana', 'cherry', 'date']

sorted_fruits = sorted(fruits, key=len) #Вместо key = lambda word: len(word)

print(f'Сортировка фруктов по длине названия {sorted_fruits}')

#4 Сумма двух чисел
add = lambda x, y: x + y
print(f'Сумма двух чисел 15 и 20 {add(15, 20)}')

#5 Переворот строки
reverse_str = lambda s: s[::-1]
print(f'Переворот строки hello {reverse_str('hello')}')
print(f'Переворот строки world {reverse_str('world')}')
print(f'Переворот строки python {reverse_str('python')}')

#6 Максимум в парах чисел
pairs = [(5, 10), (8, 3), (12, 12)]

max_in_pair = lambda x, y: max(x, y)

print(f'Максимум в парах чисел 5, 10 {max_in_pair(5, 10)}')
print(f'Максимум в парах чисел 8, 3 {max_in_pair(8, 3)}')
print(f'Максимум в парах чисел 12, 12 {max_in_pair(12, 12)}')

#7 Проверка на палиндром
pall = lambda s: s == s[::-1]
print(f'Проверка на палиндром radar {pall('radar')}')
print(f'Проверка на палиндром python {pall('python')}')
print(f'Проверка на палиндром level {pall('level')}')

#8 Количество слов в строке
count_of_words = lambda s: len(s.split())

print(f'Количество слов в строке This is a simple sentence - {count_of_words('This is a simple sentence')}')

#9 Увеличение списка на 3
three_numbers = list(map(lambda x: x + 3, numbers[:5]))

print(f'Увеличение списка на 3 - {three_numbers}')

#10 Проверка на наличие строки больше 5 символов
print(f'Проверка на наличие строки больше 5 символов {any(len(s) > 5 for s in fruits)}')