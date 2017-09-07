import json
d = {'a': 1, 'b': 2, 'c': 'cc', 12: None}
j = json.dumps(d)
print(j)

print(json.loads(j))


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student_to_json(student):
    return {'name': student.name, 'age': student.age, 'score': student.score}

s = Student('Bob', 15, 99)

print(json.dumps(s, default=student_to_json))

# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(s, default=lambda obj: obj.__dict__))




