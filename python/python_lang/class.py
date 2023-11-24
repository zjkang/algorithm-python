class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

# print(MyClass.__slots__)
print(MyClass.__dict__)



class MyClass2(object):
    def __init__(self, name, identifier):
        self.__name = name
        self.__identifier = identifier


print(MyClass2.__dict__)
my_class = MyClass2("A", "1")
print(my_class._MyClass2__name) # access the private field

