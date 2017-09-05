def f(x):
    return x % 2 == 1

print(list(filter(f, range(10))))

print(sorted([1, 10, 4, 6, -9]))
print(sorted([10, 1, 4, 6, -9], key=abs))
print(sorted([10, 1, 4, 6, -9], key=abs, reverse=True))

print(sorted(['b', 'D', 'e', '1']))
print(sorted(['b', 'D', 'e', '1'], key=str.lower))

