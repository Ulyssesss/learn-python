from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance('', Iterable))
print(isinstance((x for x in range(3)), Iterable))
print(isinstance(100, Iterable))

print('---')

print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance('', Iterator))
print(isinstance((x for x in range(3)), Iterator))
print(isinstance(100, Iterator))

print('---')

print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter(''), Iterator))
print(isinstance(iter(x for x in range(3)), Iterator))
