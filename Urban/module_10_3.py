import threading
from random import randint
from time import sleep
lock = threading.Lock()

class Bank:
    balance = 0
    def __init__(self):
        pass

    def deposit(self):
        for i in range(100):
            a = randint(50, 500)
            self.balance += a
            if self.balance >= 500 and lock.locked():
                lock.release()
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            a = randint(50, 500)
            print(f'Запрос на {a}.')
            if a <= self.balance:
                self.balance -= a
                print(f'Снятие {a}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонен, недостаточно средств')
                lock.acquire()

bk = Bank()

thread1 = threading.Thread(target=Bank.deposit, args=(bk, ))
thread2 = threading.Thread(target=Bank.take, args=(bk, ))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bk.balance}')