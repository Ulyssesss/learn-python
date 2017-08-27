d = {'Michael': 95, 1: 75, 'Jack': 60}
print(d)
print(d['Michael'])
print(d[1])
d[1] = 0
print(d)
print('xxx' in d)
print(1 in d)

print(d.get(100))
print(d.get(100, 'ccc'))

s = {1, 3, 5}
print(s)
s.add(1)
s.add(3)
s.add(7)
print(s)

s.remove(1)
print(s)

s1 = set(list(range(5)))
print(s1)

s2 = set(range(3, 6))
print(s2)

print(s1 & s2)
print(s1 | s2)

a = 'abc'
a.replace('a', 'A')
print(a)
b = a.replace('a', 'A')
print(b)