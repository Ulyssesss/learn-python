class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class FlyableMixIn(object):
    def fly(self):
        print('flying')


class RunnableMixIn(object):
    def run(self):
        print('running')


class Dog(Mammal, RunnableMixIn):
    pass


class Parrot(Bird, FlyableMixIn):
    pass


d = Dog()
p = Parrot()

d.run()
p.fly()
