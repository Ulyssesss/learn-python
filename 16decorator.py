import functools


def log(func):
    def wrapper(*args, **kw):
        print('call:', func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def hello():
    print('hello')


hello()
print(hello.__name__)


def param_log(text):
    def text_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('before', text)
            result = func(*args, **kw)
            print('after', text)
            return result
        return wrapper
    return text_log


@param_log('111')
def hi():
    print('hi')

hi()
print(hi.__name__)
