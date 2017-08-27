a = range(5)
b = range(3, 5)
print(a)
print(b)
print(list(a))
print(list(b))
print(tuple(a))
print(tuple(b))

names = ['Jack', 'Bob', 'Tony']
for name in names:
    print(name)

for x in range(10):
    print(x)

print('-----')

i = 0
while i < 3:
    print(i)
    i = i + 1

print('-----')

j = 0
while j < 100:
    print(j)
    j = j + 1;
    if j > 3:
        break

print('-----')

k = 0
while k < 10:
    k = k + 1
    if k % 2 == 0:
        continue
    print(k)

