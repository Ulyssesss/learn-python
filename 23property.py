class Student1(object):

    def __init__(self):
        self._score = None

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score

    def get_score(self):
        return self._score

s1 = Student1()
# s1.set_score('1')
# s1.set_score(200)
s1.set_score(99)
print(s1.get_score())


class Student2(object):

    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score

s2 = Student2()
# s2.score = 'a'
# s2.score = 101
s2.score = 100
print(s2.score)
