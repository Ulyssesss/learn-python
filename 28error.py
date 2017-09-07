import logging
logging.basicConfig(level=logging.DEBUG)
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
# except捕获该类型及其子类错误
except ValueError as e:
    # logging.exception(e)
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value')
    return 10 / n

try:
    foo(0)
except FooError as e:
    pass
    # logging.exception(e)
    # raise
    # raise语句如果不带参数，就会把当前错误原样抛出

'''
日志级别：
critical > error > warning > info > debug, notset
级别越高打印的日志越少
'''
logging.info('info')
logging.debug('debug')
logging.error('error')
print('END')
