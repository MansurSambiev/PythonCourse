from pprint import pprint
import inspect


def introspection_info(obj):
    pprint(type(obj))
    pprint(dir(obj))
    pprint(inspect.getmodule(obj))

class New:
    def __init__(self, x):
        self.x = x

    def square_x(self):
        return self.x**2

some_class_obj = New(2)
introspection_info(some_class_obj)
