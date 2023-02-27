from collections import defaultdict

d = defaultdict(list)

data = (['a', 1, 1], ['b', 2, 3], ['c', 15, 125], ['b', 22, 158])

for key, value_1, value_2 in data:
    d[key].append(value_1)
    d[key].append(value_2)

print(d)
