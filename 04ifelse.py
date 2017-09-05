age = 20
print('your age is', age)
if age > 18:
    print('adult')
elif age > 6:
    print('teenager')
else:
    print('kid')

if -1:
    print('-1 True')

if not 0:
    print('0 False')

if [1, 2]:
    print('[1, 2] True')

if not []:
    print('[] False')

if 'a':
    print('\'a\' True')

if not '':
    print('\'\' False')

birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')

