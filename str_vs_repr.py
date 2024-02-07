class my_class():
    def __init__(self):
        pass

    def __str__(self):
        return 'dunder str was called!'

    def __repr__(self):
        return 'dunder repr was called!'


obj = my_class()
print(obj)
print(str(obj))
print(f'Hello.  {obj}')
