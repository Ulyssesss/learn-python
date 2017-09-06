print(type(123))
print(type(''))
print(type(None))


class Animal(object):
    def __init__(self):
        self.name = 'cc'
        self.__name = 'cc'

    def __len__(self):
        return 1

a = Animal()

print(type(a))
print(type(a) == Animal)
print(type(111) == int)

print(type(a) == object)
print(isinstance(a, object))

print(dir('abc'))
print(dir(a))

print(len('ABC'))
print('ABC'.__len__())

print(hasattr(a, 'name'))
print(hasattr(a, '__name'))

print(getattr(a, 'name'))
setattr(a, 'name', 'dd')
print(getattr(a, 'name'))
print(getattr(a, '__name', 'ee'))


class Student(object):
    name = 'student'

    def __init__(self, name):
        self.name = name

a = Student('Bob')
a.score = 90

print(a.name)
print(a.score)

print(Student.name)
a.name = 'Mark'
print(a.name)
print(Student.name)

del a.name

print(a.name)
