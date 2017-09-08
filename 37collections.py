from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ('x', 'y'))
p = Point(1, 2)
print(p.x)
print(p.y)
print(type(p))
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
l = [1, 2, 3, 4, 'x', 'y']
q = deque(l)
q.popleft()
q.popleft()
print(q)

d = defaultdict(lambda: None)
print(d['a'])

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
o = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(o)
a = o.popitem(last=False)
print(a)
print(o)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
