from functools import reduce

x = lambda x, y: x + y
print(x(2, 4))

userInfo = lambda name, age: f'Имя {name}, возраст {age}'
print(userInfo)

#map осуществляет действие (1й аргумент) над передаваемым объектом (2й аргумент)
nums = ['1', '2', '3']
nums = [1, 2, 3]
new_nums = list(map(int, nums))
new_nums_map = list(map(lambda x: x**2, nums))
print(new_nums)

tempC = [21, 17, 16, 19, 14, 10]


def fahr(temp):
    return round(temp * 1.8 + 32, 2)


new_temp = list(map(fahr, tempC))

print(new_temp)


def fiter_nums(num):
    return num > 2


numbers = [1, 2, 3, 4, 5]

new_num = list(filter(fiter_nums, numbers))
print(new_num)
new_num_filter = list(filter(lambda x: x > 2, numbers))
print(new_num_filter)

#ilter возвращает элементы из объекта для которых функция вернула истину (третий аргумент начальное значение переменной)
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


numbers = [1, 2, 3, 4, 5]
#
new_num = list(reduce(add, numbers, 0))
print(new_num)

mult_num = list(reduce(multiply, numbers))
mult_num_reduce = reduce(lambda x, y: x * y, numbers)
print(mult_num_reduce)