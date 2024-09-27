class Point:

    # Вызывается перед созданием экземпляра класса
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    #Инициализация класса, вызывается сразу после создания объекта
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Получение свойств item
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    #Изменение свойства key
    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

    #Получение не существующего свойства item
    def __getattr__(self, item):
        return False

    #Удаление свойства item
    def __delattr__(self, item):
        object.__delattr__(self, item)

    @classmethod  # методы используется для работы с атрибутами класса
    def metodclassa(cls):
        return
        pass


    @staticmethod  # Используется для создания методов, не связанных с самим классом и его атрибутами
    def metodstat(cls):
        return
        pass

pt1 = Point(1, 2)


# #Свойства аргументов
# public -> arg доступен отовсюду
# protected -> _arg доступен только внутри самого класса и его дочерних
# private -> __arg

