classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[0])
print(classmates[-1])
print(len(classmates))

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)

classmates[0] = 'Sarah'
print(classmates)

l = ['Apple', 1, True]
print(l)

s = [1, 2, [3, 4], 5]
print(len(s))

e = []
print(len(e))

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
print([k + '=' + v for k, v in {'a': '1', 'b': '2'}.items()])
