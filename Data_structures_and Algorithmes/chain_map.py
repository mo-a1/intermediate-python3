from collections import ChainMap

values = ChainMap()
values['x'] = 1

print(values)
values = values.new_child()
print(values)
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
values = values.parents
values = values.parents
print(values)

print('s2' * 20)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 33, 'e': 4, 'f': 5, 'g': 6}

all_dicts = ChainMap(dict2, dict1)
print(all_dicts)

print(len(all_dicts))
print(all_dicts['c'], '_____c')
print(all_dicts['a'], '_____a')

print(all_dicts.items())

for key, value in all_dicts.items():
    print('key', key)
    print('value', value)
    print('_' * 20)
