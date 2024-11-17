import threading
#Модуль работы с потоками
from time import sleep
#Модуль работы со временем

def func1():
    for i in range(10):
        sleep(0.5)
        #Остановка на указанное время в секундах
        print(i, threading.current_thread())
        #Вывод текущего потока

def func2(x):
    for i in range(10):
        sleep(1)
        print(i, threading.current_thread())
        print(threading.current_thread().is_alive())

thread = threading.Thread(target=func2, args=(1,), daemon=True)
#Создание нового потока, указываем выполняемую функцию в этом потоке, передаваемые аргументы
# поток-демон завершается, когда завершаются остальные потоки, даже если он не выполнился полностью
thread.start()
#Запуск потока. Без этого он будет висеть "в ожидании"
#thread.join()
#Приостановка основного потока, пока не выполнится дополнительный
func1()

print(threading.enumerate())
#Вывод списка запущенных потоков
print(threading.current_thread())