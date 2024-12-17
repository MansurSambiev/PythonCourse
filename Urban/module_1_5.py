immutable_var = (1, '2', True, 3.14)
print(immutable_var)
immutable_var[1] = '3'
#Кортеж является неизменяемы типом данных и не поддреживает изменение отдельно взятых элементов

mutable_list = ['apple', 'kiwi', 5, False]
print(mutable_list)
mutable_list[3] = True
print(mutable_list)
