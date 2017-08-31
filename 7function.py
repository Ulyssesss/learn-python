# help(abs)
print(abs(-1))
print(max(1, 2, 3, 4, -5, -6, 1))
print(int(1.2))
print(str(12))
print(float(1))
print(bool(1))
print(bool(''))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        print(x)
    else:
        print(-x)

my_abs(-1.1)


def my_pass():
    pass

my_pass()


def return2():
    return 1, 2

print(return2())
print(return2()[1])


def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(5, 2))


def power2(x, n=2):
    # 默认参数必须指向不变对象
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power2(5, 3))
print(power2(5))


def calc(*numbers):
    result = 0
    for n in numbers:
        result = result + n * n
    return result

print(calc(1, 2, 3))
t = (1, 2, 3)
print(calc(*t))


def person1(name, age, **other):
    print("name:", name, "age:", age, "other:", other)

person1("Jack", 18)
person1("Jack", 18, city='Beijing', country='China')
d = {'city': 'Beijing', 'country': 'China'}
person1('Jack', 18, **d)


def person2(name, age, *, city, country):
    print("person2 name:", name, "age:", age, "city:", city, "country:", country)

person2('Jack', 18, city='Beijing', country='China')

# 组合参数顺序：位置参数、默认参数、可变参数、命名关键字参数和关键字参数
# 命名关键字参数可在参数较多时不按顺序赋值，更加灵活


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, arg, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'arg =', arg, 'kw =', kw)


f1(1, 2, 3, 4, 5, 6, 7, other=1)
f2(1, 2, 3, arg=4, other=1)

t = (1, 2, 3)
d = {'arg': 4, 'other': 1}
f2(*t, **d)
