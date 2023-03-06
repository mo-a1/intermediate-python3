import pprint

lis = [i for i in range(20)]
lis2 = [i for i in range(90)]
pprint.pprint(lis)
pprint.pprint(lis2)

dct = {}
for i, j in enumerate(range(999, 1010)):
    dct[i] = j
    if j == 1000:
        dct[i] = [x for x in range(20)]
    if j == 1001:
        dct[(x for x in range(20))] = [x for x in range(5)]

pprint.pprint(dct)

pprint.pp("pprint.pp(dct)")
pprint.pp(dct)
