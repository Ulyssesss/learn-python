import os

print(os.name)
print(os.uname())

print(os.environ)
print(os.environ.get('PATH'))

p = os.path.join('.', 'test_dir')
print(p)
os.mkdir(p)
os.rmdir(p)
