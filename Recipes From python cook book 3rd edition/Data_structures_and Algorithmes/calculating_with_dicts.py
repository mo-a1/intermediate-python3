dic = {
    'a': 1024,
    'b': 254,
    'c': 125874,
    'f': 23,
}

print([i for i in zip(dic.keys(), dic.values())])

max_in_dic = max(zip(dic.keys(), dic.values()))
min_in_dic = min(zip(dic.keys(), dic.values()))

print(max_in_dic)
print(min_in_dic)

max_in_dic = max(zip(dic.values(), dic.keys()))
min_in_dic = min(zip(dic.values(), dic.keys()))

print(max_in_dic)
print(min_in_dic)

# Finding commonalities

dic_2 = dic = {
    'g': 12,
    'b': 254,
    'm': 1,
    'f': 23,
}

print(dic_2.keys() - dic.keys())
print(dic_2.items() & dic.items())

a = [1, 1, 58, 2, 3, 5, 6, 2, 9, 8, 3, 7, 52]
b = list(set(a))
print(b)

l = [{'a': 1, 'b': 2}, {'a': 3, 'b': 2}, {'a': 6, 'b': 2}, {'a': 1, 'b': 2}, {'a': 3, 'b': 4}]


def dedup(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


print(list(dedup(l, key=lambda a: (a['a'], a['b']))))
print(list(dedup([1, 2, 3, 1, 2, 5])))
