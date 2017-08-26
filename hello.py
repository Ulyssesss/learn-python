#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello, world')
print('The quick brown fox', 'jumps over', 'the lazy dog')
print('100 + 200 =', 100 + 200)
# name = input('please enter your name: ')
# print('hello,', name)

# comment

print(1.26)
print(-200)
print(0xfff)
print('I\'m \"OK\"!')
print('\\')
print(r'\\\\\\')
print('''line1
line2
line3''')

print(True and True)
print(5 + 3 > 6 and 1 == 0)
print(not False)

if 5 > 3:
    print(5)
    print('code block')
else:
    print(3)

print(None)

a = 1
b = a
a = 'aaa'
print(b)

print(10 / 3)
print(10 // 3)
print(10 % 3)

print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')
print(b'ABC')

print('--------')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))

print(len('abc'))
print(len('中文'))
print(len('中文'.encode('utf-8')))

print('整数: %05d \n浮点数: %.3f \n字符串: %s' % (1, 2.5, 'aaa'))

print('%.2f%%' % ((85 - 72) / 72 * 100))

