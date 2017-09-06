from types import MethodType


class Student1(object):
    pass

s1 = Student1()
s1.name = 'Michael'
print(s1.name)


def set_age(self, age):
    self.age = age

# 给实例绑定方法
s1.set_age = MethodType(set_age, s1)

s1.set_age(25)
print(hasattr(s1, 'set_age'))
print(s1.age)

s2 = Student1()
print(hasattr(s2, 'set_age'))


def set_score(self, score):
    self.score = score

# 给类绑定方法
Student1.set_score = set_score
s1.set_score(99)
s2.set_score(91)
print(s1.score)
print(s2.score)


class Student2(object):
    __slots__ = ('name', 'age')

s3 = Student2()

s3.name = 'Jack'
s3.age = 16

# 'Student2' object has no attribute 'score'
# s3.score = 99

# __slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


