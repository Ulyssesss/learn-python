class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):
    def run(self):
        print('dog is running')


class Cat(Animal):
    def run(self):
        print('cat is running')


a = Animal()
b = Dog()
c = Cat()

a.run()
b.run()
c.run()

print(isinstance(a, Animal))
print(isinstance(b, Animal))
print(isinstance(c, Animal))

print(isinstance(a, Dog))
print('---')


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(a)
run_twice(b)
run_twice(c)


class CanRun(object):
    def run(self):
        print('running')

run_twice(CanRun())
