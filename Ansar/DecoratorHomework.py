#Написать декоратор удваивающий результат функции
def double_result(func):
    def wrapper(*args):
        result = func(*args) * 2
        return result

    return wrapper

@double_result
def add(a, b):
    return a + b

print(add(2, 3))

#Декоратор приветствия
def greet_decorator(func):
    def wrapper(*args):
        print("Приветствую!")
        func(*args)

    return wrapper

@greet_decorator
def say_name(name):
    print(f'Меня зовут {name}')

@greet_decorator
def say_goodbye():
    print('До свидания!')

say_name('John')
say_goodbye()