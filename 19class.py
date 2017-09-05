class Student1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print(self.name, self.score)

a = Student1('Jack', 98)
a.print()
print(a.name, a.score)


class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print(self):
        print(self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if score >= 0:
            self.__score = score

b = Student2("Mark", 97)
b.print()
print(b.get_name(), b.get_score())
b.set_name("Tony")
b.set_score(96)
b.set_score(-1)
b.print()
