try:
    f = open('test_io', 'r')
    print('read line', f.readline())
    print(f.read())
finally:
    if f:
        f.close()

print('---')

with open('test_io', 'r', encoding='utf-8', errors='ignore') as f:
    l = f.readlines()
    for i in l:
        print('read lines', i)


with open('test_io', 'w') as f:
    f.write('Hello, world!\n')
    f.write('test1\n')
    f.write('test2\n')
    f.write('test3\n')

from io import StringIO

s = StringIO()
s.write('aaa')
s.write('bbb')
print(s.getvalue())
