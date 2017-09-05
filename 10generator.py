g = (x * x for x in range(10))

for n in g:
    print(n)

a = 1
b = 2
a, b = b, a + b
print(a, b)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))

print('-----')

for o in odd():
    print(o)