class my_class():
    def __init__(self):
        self._name = "my class"

    def __str__(self):
        return f'dunder str was called on {self._name}'

    def __repr__(self):
        return f'dunder repr was called on my_class({self._name})'


obj = my_class()
print(obj) # -> 'dunder str was called!'
print(str(obj)) # -> 'dunder str was called!'
print(f'{obj}') # -> 'dunder str was called!'
print(repr(obj)) # -> 'dunder repr was called!
