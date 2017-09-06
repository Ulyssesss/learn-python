class Hello(object):

    def hello(self, text='world'):
        print('hello,', text)

h = Hello()

print(type(h))
print(type(Hello))
print('---')


def fn(text):
    print('hello,', text)

Hello2 = type('Hello2', (object, ), dict(hello=fn))
h2 = Hello2()
print(type(h2))
print(type(Hello2))
