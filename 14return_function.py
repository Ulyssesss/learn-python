def f1(*args):
    def g():
        result = 0
        for n in args:
            result = result + n
        return result
    return g

r1 = f1(1, 2, 3, 4)

print(r1)
print(r1())


def f2():
    l = []
    for i in range(1, 4):
        def g():
             return i * i
        l.append(g)
    return l

r2, r3, r4 = f2()

print(r2())
print(r3())
print(r4())
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量

print('---')

# 再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变


def f3():
    l = []
    for i in range(1, 4):
        def g(i):
            def h():
                return i * i
            return h
        l.append(g(i))
    return l

r5, r6, r7 = f3()
print(r5())
print(r6())
print(r7())
