from collections import Counter

a = Counter()                           # a new, empty counter
b = Counter('abd allah')                # a new counter from an iterable (string)
b_ = Counter(["ali", "sayed", "ali"])   # a new counter from an iterable (list, ..)
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
d = Counter(cats=4, dogs=8)             # a new counter from keyword args

print(b_)
print(c)
print([i for i in c.elements()])
print(b)
print(b.most_common(1))
print(d)
print(d.total())
