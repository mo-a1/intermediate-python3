from collections import namedtuple

user = namedtuple('visitor', ['name', 'age'])

user1 = user('ali', 12)
print(user1)

a, b = user1
print(a)
print(b)

data = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', None)]


def trans(data):
    t = namedtuple('row', ['litter', 'num'])
    result = []
    for tuble_ in data:
        temp = t(*tuble_)
        result.append(temp)
    return result


print(trans(data))
