import functools
print(int('123456'))
print(int('1001001', base=2))


def int2(x, base=2):
    return int(x, base)

print(int2('100'))

int8 = functools.partial(int, base=8)

print(int8('77'))

kw = {'base': 16}
int16 = functools.partial(int, **kw)

print(int16('ff'))
