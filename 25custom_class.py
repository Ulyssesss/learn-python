class Student(object):
    def __init__(self, name):
        self.name = name
        self.a = 0
        self.b = 1

    def __str__(self):
        return 'name: ' + self.name

# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            return 'a'
        if isinstance(item, slice):
            return self.name[item]

    def __getattr__(self, item):
        if item == 'age':
            return 16

    def __call__(self, *args, **kwargs):
        print('call')

s1 = Student('Mark')
print(s1)
i = iter(s1)
for x in range(10):
    print(next(i))

print(s1[1])
print(s1['aa'])
print(s1[0:1])

print(getattr(s1, 'name'))
print(getattr(s1, 'age'))
print(getattr(s1, 'gender'))
print('---')
print(s1.name)
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
print(s1.abc)

if callable(s1):
    s1()


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().a.b.c.d)
