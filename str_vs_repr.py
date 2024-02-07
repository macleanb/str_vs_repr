class class_with_repr():
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f'dunder str was called on {self._name}'

    def __repr__(self):
        return f'dunder repr was called on class_with_repr({self._name})'

class class_without_repr():
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return f'dunder str was called on {self._name}'


repr_obj_one = class_with_repr('Object 1')
repr_obj_two = class_with_repr('Object 2')
print(repr_obj_one) # -> 'dunder str was called on Object 1'
print(str(repr_obj_one)) # -> 'dunder str was called on Object 1'
print(f'{repr_obj_one}') # -> 'dunder str was called on Object 1'
print(repr(repr_obj_one)) # -> 'dunder repr was called on class_with_repr(Object 1)'
my_list = [repr_obj_one, repr_obj_two] # -> '[dunder repr was called on class_with_repr(Object 1), dunder repr was called on class_with_repr(Object 2)]'
print(my_list)

no_repr_obj = class_without_repr('Object 3')
print(no_repr_obj) # -> 'dunder str was called on Object 3'
print(str(no_repr_obj)) # -> 'dunder str was called on Object 3'
print(f'{no_repr_obj}') # -> 'dunder str was called on Object 3'
print(repr(no_repr_obj)) # -> '<__main__.class_without_repr object at 0x100c35710>'
my_list = [no_repr_obj] # -> '[<__main__.class_without_repr object at 0x100c35710>]'
print(my_list)
