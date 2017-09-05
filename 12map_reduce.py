from functools import reduce

x = abs


def abs_add(a, b, c):
    print(c(a) + c(b))

abs_add(1, -2, x)


def f(i):
    return i * i

print(list(map(f, range(5))))


def add(j, k):
    return j + k

print(reduce(add, range(5)))
