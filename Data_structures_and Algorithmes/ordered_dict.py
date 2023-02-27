from collections import OrderedDict

d = OrderedDict()

d['sayed'] = 10
d['hany'] = 0
d['ahmed'] = 1
d['mona'] = 5

for key, value in d.items() :
    print(key, value)

print(d.popitem(last=True))
print(d.popitem(last=False))
print(d)
